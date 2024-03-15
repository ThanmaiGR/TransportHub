import random
import datetime
import decimal
import heapq
from django.db.models import F
from .models import Locations, Connections, RouteDetails, CabCompanies, CabFareStructure, Routes
from django.db import connection


def normalize(value_1, value_2):
    """
    Normalize 2 values to range [0,1]

    :param value_1: The First Value
    :param value_2: The Second Value
    :return: Normalized Values of value_1 and value_2
    """
    min_val = min(value_1, value_2)
    max_val = max(value_1, value_2)
    if max_val != min_val:
        normalized_first = (value_1 - min_val) / (max_val - min_val)
        normalized_second = (value_2 - min_val) / (max_val - min_val)
    else:
        # If both values are the same, set normalized values to 0.5
        normalized_first = 0.5
        normalized_second = 0.5
    return normalized_first, normalized_second


def get_location_name(start_id, stop_id):
    """
    Retrieve the names of start and stop locations based on their IDs.

    :param start_id: The ID of the start location.
    :param stop_id: The ID of the stop location.
    :return: A tuple containing the names of the start and stop locations
    """

    with connection.cursor() as cursor:
        cursor.execute("CALL GetLocationName(%s, %s)", [start_id, stop_id])
        result = cursor.fetchall()[0]
    return result


def get_route_name(route_id):
    """
    Retrieve the name of a route based on its ID.

    :param route_id: The ID of the route.
    :return: The name of the route.
    """

    with connection.cursor() as cursor:
        cursor.execute("CALL GetRouteName(%s)", [route_id])
        result = cursor.fetchall()[0][0]
    return result


def enhance_path_info(actual_path):
    """
    Enhances the given path with additional information.

    Each row in the path is augmented with location names, route names, and vehicle types
    retrieved from the ORM models.

    :param actual_path: A list of path details in the format [start_id, stop_id, route_id, fare, time].
    :return: The enhanced path with additional information.
    """

    for idx, row in enumerate(actual_path):
        start_id, stop_id, route_id, time = row[0], row[1], row[2], row[4]
        # row[0] = Locations.objects.filter(LocationID=start_id).values_list(
        #     'LocationName',
        #     flat=True
        # ).first()
        # row[1] = Locations.objects.filter(LocationID=stop_id).values_list(
        #     'LocationName',
        #     flat=True
        # ).first()

        row[0], row[1] = get_location_name(start_id, stop_id)
        row[2] = get_route_name(route_id)
        row[4] = str_to_time(time)
        vehicle_type = Routes.objects.filter(RouteID=route_id).values_list(
            'VehicleType',
            flat=True
        ).first()
        row.insert(3, vehicle_type)
        actual_path[idx] = row
    return actual_path


def str_to_time(time):
    """
    Converts a time represented as a string to the format H:MM.
    :param time: A string representing time in hours.
    :return: A string representing time in the format H:MM.
    """
    hours = int(time)
    minutes = (time * 60) % 60
    seconds = (time * 3600) % 60
    if seconds > 40:
        minutes += 1
    return "%d:%02d" % (hours, minutes)


def find_path(source, destination, path):
    """
    Returns the route from the destination node to the source node based on the provided path dictionary.

    :param source: The source node.
    :param destination: The destination node.
    :param path: A dictionary containing information about the next nodes for each node.
    :return: The route from the destination to the source node.
    """

    path_dict = {}
    current_stop = destination

    while current_stop != source:
        next_stop = path[current_stop]['from']
        route_id = path[current_stop]['by']
        fare = path[current_stop]['fare']
        time = path[current_stop]['time']
        path_dict[current_stop] = {
            "next_stop": next_stop,
            "route_id": route_id,
            "fare": fare,
            "time": time
        }

        current_stop = next_stop

    # Add the source to the path dictionary with a route ID of None
    path_dict[source] = {
        "next_stop": None,
        "route_id": None,
        "fare": 0,
        "time": 0
    }

    return path_dict


def go_from_source_to_destination(source, destination, path):
    """
    Returns the route from the source node to the destination node using the provided path dictionary.

    :param source: The source node.
    :param destination: The destination node.
    :param path: A dictionary containing information that can be used to traverse from the destination node to the
    source node.
    :return: The route from the source node to the destination node.
    """

    current_stop = source
    route = []

    while current_stop is not None:
        route.append(
            [
                path[current_stop]['next_stop'],
                current_stop,
                path[current_stop]['route_id'],
                path[current_stop]['fare'],
                path[current_stop]['time']
            ]
        )
        if current_stop == destination:
            break
        next_stop = path[current_stop]['next_stop']
        current_stop = next_stop
    route.pop()
    route.reverse()
    return route


def generate_traffic(current_time=None):
    """
    Generates a traffic factor based on the given current time.

    :param current_time: The time at which the traffic factor is to be generated.
    :return: The traffic factor calculated for the given time.
    """

    if current_time is None:
        current_time = datetime.datetime.now()

    # Define base probabilities for each traffic level
    base_traffic_probabilities = {
        "low": 0.1,
        "medium": 0.3,
        "high": 0.6
    }

    # Adjust probabilities based on time of day
    random_number = random.random()
    if 15 <= current_time.hour < 19:  # Rush hours in the evening
        if random_number < 0.35:
            base_traffic_probabilities["low"] /= 0.8
        elif random_number < 0.75:
            base_traffic_probabilities["medium"] /= 1.2
        else:
            base_traffic_probabilities["high"] /= 2.0
    elif 7 <= current_time.hour < 10:  # Morning rush hours
        if random_number < 0.35:
            base_traffic_probabilities["low"] /= 0.8
        elif random_number < 0.75:
            base_traffic_probabilities["medium"] /= 1.5
        else:
            base_traffic_probabilities["high"] /= 1.8

    # Adjust probabilities based on the day of the week
    weekday = current_time.weekday()  # Monday is 0, Sunday is 6
    random_number = random.random()
    if weekday < 5:  # Weekdays
        if random_number < 0.35:
            base_traffic_probabilities["low"] /= 1.2
        elif random_number < 0.75:
            base_traffic_probabilities["medium"] /= 1.4
        else:
            base_traffic_probabilities["high"] /= 1.6
    else:  # Weekends
        if random_number < 0.35:
            base_traffic_probabilities["low"] /= 0.8
        elif random_number < 0.75:
            base_traffic_probabilities["medium"] /= 0.8
        else:
            base_traffic_probabilities["high"] /= 0.8

    # Introduce random event probability
    random_event_probability = random.uniform(0.01, 0.1)  # 5% chance of a random event affecting traffic
    if random.random() < random_event_probability:
        # Adjust probabilities for random event
        random_event_type = random.choice(["protest", "accident", "road_closure"])
        if random_event_type == "protest":
            base_traffic_probabilities["high"] /= 2.1
            base_traffic_probabilities["medium"] *= 1.2
            base_traffic_probabilities["low"] *= 0.8
        elif random_event_type == "accident":
            base_traffic_probabilities["high"] /= 1.5
            base_traffic_probabilities["medium"] /= 1.2
            base_traffic_probabilities["low"] *= 0.8
        elif random_event_type == "road_closure":
            base_traffic_probabilities["high"] /= 2
            base_traffic_probabilities["medium"] /= 1.5
            base_traffic_probabilities["low"] /= 1.2

    # Generate a random number between 0 and 1
    random_number = random.random()

    # Determine traffic level based on adjusted probabilities
    cumulative_probability = 0
    for level, probability in base_traffic_probabilities.items():
        cumulative_probability += probability
        if random_number <= cumulative_probability:
            return base_traffic_probabilities[level]

    # Default to low traffic if no match found
    return base_traffic_probabilities['high']


class Graph:
    """
    Represents a graph for modeling transportation networks.

    Attributes:
        adjacency_list (dict): A dictionary representing the adjacency list of the graph.
        cost_list (dict): A dictionary containing the cost (e.g., fare) for traveling between nodes.
        traffic (dict): A dictionary containing traffic information for each edge.
        speed (dict): A dictionary containing the speed of different transportation modes.

    Methods:
        __init__(self, time): Initializes the Graph object with given time information.
        add_traffic(self, time): Calculates the traffic factor for each edge based on the given time.
        add_location(self, location_id): Creates an adjacency list of all edges connected to the given location.
        add_cost_and_factor(self, source_id, destination_id, distance): Calculates cost and traffic factor for edges.
        calculate_best_path(self, source, destination, main_factor="Both"): Calculates the best path between
            source and destination nodes based on a specified factor.
        find_cabs(self, source, destination): Calculates the total fare and time taken by each cab to travel from
            source node to destination node.
        calculate_cab_distance(self, source, destination): Calculates the total distance and time taken by a cab to
            reach the destination from the source node.
    """

    def __init__(self, time):
        """
        Initializes a Graph object with the provided time.

        This method sets up the graph by:
        - Initializing the adjacency list, cost list, and traffic dictionaries.
        - Retrieving locations and adding them to the adjacency list.
        - Setting up the speed dictionary for different transportation modes.
        - Adding traffic information based on the provided time.
        - Adding cost and traffic factor for each edge.

        :param time: The time at which the graph is initialized, used for calculating traffic.
        """
        self.adjacency_list = {}
        self.cost_list = {}
        self.traffic = {}
        locations = Locations.objects.all()
        self.speed = {
            'Bus': 30,
            'Metro': 50
        }
        for location in locations:
            self.add_location(location.LocationID)
        edges = Connections.objects.all()
        self.add_traffic(time)
        for edge in edges:
            self.add_cost_and_factor(
                edge.SourceID_id,
                edge.DestinationID_id,
                edge.Distance,
            )

    def add_traffic(self, time):
        """
        Calculates the traffic factor for each edge based on the given time.

        :param time: The time at which the travel takes place.
        :return: None
        """

        for key, value in self.adjacency_list.items():
            for node in value:
                traffic_factor = generate_traffic(time)
                if key not in self.traffic:
                    self.traffic[key] = {}
                self.traffic[key][node[0]] = traffic_factor

    def add_location(self, location_id):
        """
        Creates an adjacency list of all edges connected to the given location_id.

        :param location_id: The location_id of a location.
        :return: None
        """

        self.adjacency_list[location_id] = []
        self.adjacency_list[location_id].extend([
            (connection.DestinationID_id, connection.Distance)
            for connection in Connections.objects.filter(SourceID_id=location_id)
        ])

    def add_cost_and_factor(self, source_id, destination_id, distance):
        """
        Finds all paths to a neighbor node along with route number, fare, and time taken to reach the neighbor.

        :param source_id: The current node.
        :param destination_id: The neighbor node.
        :param distance: The distance between the source and destination.
        :return: None
        """

        route_fares = RouteDetails.objects.filter(
            RouteID__in=RouteDetails.objects.filter(StopID=source_id).values('RouteID'),
            StopID=destination_id
        ).select_related('RouteID').annotate(
            FarePerKM=F('RouteID__FarePerKM'),
            VehicleType=F('RouteID__VehicleType')
        ).values('RouteID', 'VehicleType', 'FarePerKM')

        if source_id not in self.cost_list:
            self.cost_list[source_id] = {}
        self.cost_list[source_id][destination_id] = []
        if not route_fares:
            del self.cost_list[source_id][destination_id]
        for each_fare in route_fares:
            fare = each_fare['FarePerKM'] * distance
            route_id = each_fare['RouteID']
            vehicle = each_fare['VehicleType']
            usual_time = distance / self.speed[vehicle]
            if vehicle == 'Bus':
                modified_time = (usual_time
                                 + (usual_time * decimal.Decimal(self.traffic[source_id][destination_id])))
                norm_fare, norm_time = normalize(fare, decimal.Decimal(modified_time))
                factor = decimal.Decimal(0.8) * norm_fare + decimal.Decimal(0.2) * norm_time
                self.cost_list[source_id][destination_id].append((route_id, fare, modified_time, factor))
            else:
                norm_fare, norm_time = normalize(fare, decimal.Decimal(usual_time))
                factor = decimal.Decimal(0.2) * norm_fare + decimal.Decimal(0.8) * norm_time
                self.cost_list[source_id][destination_id].append((route_id, fare, usual_time, factor))

    def calculate_best_path(self, source, destination, main_factor="Both"):
        """
        Calculates the best path between the source and destination nodes based on a specified factor.

        :param source: The starting node.
        :param destination: The destination node.
        :param main_factor: The factor to use for calculation, such as fare, time, or a combination of both.
        :return: A tuple containing the total fare, total time, and the path between the source and destination nodes.
        """

        factors = {
            "Fare": 1,
            "Time": 2,
            "Both": 3
        }
        if main_factor == "Both":
            other_factor = "Fare"
        else:
            other_factor = "Both"
        pq = [(0, 0,
               source)]  # The first element is the total fare, the second is the total time and third is location_id
        path_taken = {}
        total_fare = {location_id: float('inf') for location_id in self.adjacency_list}
        total_time = {location_id: float('inf') for location_id in self.adjacency_list}
        total_factor = {location_id: float('inf') for location_id in self.adjacency_list}

        total_fare[source] = 0
        total_time[source] = 0
        while pq:
            current_fare, current_time, current_location_id = heapq.heappop(pq)

            if current_location_id == destination:
                return total_fare[destination], total_time[destination], path_taken

            for neighbor_id, distance in self.adjacency_list[current_location_id]:
                if neighbor_id in path_taken:
                    continue
                if (current_location_id in self.cost_list
                        and neighbor_id in self.cost_list[current_location_id]):
                    route_id, fare, time_taken, both = min(self.cost_list[current_location_id][neighbor_id],
                                                           key=lambda x: (
                                                               x[factors[main_factor]],
                                                               x[factors[other_factor]]
                                                           ))
                    if main_factor == 'Both':
                        deciding_value = both
                    elif main_factor == 'Fare':
                        deciding_value = fare
                    else:
                        deciding_value = time_taken

                    new_fare = current_fare + fare
                    new_time = current_time + time_taken
                    if deciding_value < total_factor[neighbor_id]:
                        total_fare[neighbor_id] = new_fare
                        total_time[neighbor_id] = new_time
                        total_factor[neighbor_id] = deciding_value
                        heapq.heappush(pq, (new_fare, new_time, neighbor_id))
                        path_taken[neighbor_id] = ({
                            'from': current_location_id,
                            'by': route_id,
                            'fare': fare,
                            'time': time_taken
                        })
        return float('inf'), None, None

    def find_cabs(self, source, destination):
        """
        Calculates the total fare and time taken by each cab to travel from the source node to the destination node.

        :param source: The source node.
        :param destination: The destination node.
        :return: A dictionary containing the total fare and time taken by each cab to go from the source to the
        destination.
        """

        cab_fares = {}
        cabs = CabFareStructure.objects.all()
        total_distance, total_time = self.calculate_cab_distance(source, destination)
        time = str_to_time(total_time)
        for cab in cabs:
            base_price = cab.BasePrice
            company_id = cab.CompanyID_id
            price_per_km = cab.PricePerKM
            base_km = cab.BaseKM
            cab_name = CabCompanies.objects.filter(CompanyID=company_id).values_list('CompanyName').first()
            if total_distance < base_km:
                total_fare = base_price
            else:
                total_fare = (base_price
                              + ((total_distance - base_km)
                                 * price_per_km))
            cab_fares[cab_name[0]] = (total_fare, time)
        return cab_fares

    def calculate_cab_distance(self, source, destination):
        """
        Calculates the total distance and time taken by a cab to reach the destination from the source node.

        :param source: The source node.
        :param destination: The destination node.
        :return: A tuple containing the total distance and time taken by the cab to reach the destination from the
         source.
        """

        cab_speed = 45
        pq = [(
            0,
            0,
            source
        )]  # The first element is the total fare, the second is the total time and third is location_id
        total_distance = {location_id: float('inf') for location_id in self.adjacency_list}
        total_time = {location_id: float('inf') for location_id in self.adjacency_list}
        total_distance[source] = 0
        total_time[source] = 0
        while pq:
            current_distance, current_time, current_location_id = heapq.heappop(pq)

            if current_location_id == destination:
                return total_distance[destination], total_time[destination]

            for neighbor_id, distance in self.adjacency_list[current_location_id]:
                time_factor = decimal.Decimal(self.traffic[current_location_id][neighbor_id])
                usual_time = distance / cab_speed
                time_taken = usual_time + (time_factor*usual_time)
                new_distance = current_distance + distance
                new_time = current_time + time_taken
                if new_distance < total_distance[neighbor_id]:
                    total_distance[neighbor_id] = new_distance
                    total_time[neighbor_id] = new_time
                    heapq.heappush(pq, (new_distance, new_time, neighbor_id))

        return float('inf'), None
