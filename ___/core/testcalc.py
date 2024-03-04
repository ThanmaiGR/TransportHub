import decimal
import heapq
from django.db.models import F
from django.db import models
from .Functions import generate_traffic, str_to_time
from .models import Locations, Routes, Connections, RouteDetails, CabCompanies, CabFareStructure


class Graph:
    def __init__(self, time):
        self.adjacency_list = {}
        self.cost_list = {}
        self.traffic = {}
        locations = Locations.objects.all()
        self.speed = {
            'Bus': 30,
            'Metro': 50
        }
        for location in locations:
            self.add_location(
                location.LocationID,
                location.Latitude,
                location.Longitude
            )
        edges = Connections.objects.all()
        self.add_traffic(time)
        for edge in edges:
            self.add_cost_and_factor(
                edge.SourceID_id,
                edge.DestinationID_id,
                edge.Distance,
                time
            )
        # print('________________________________-')
        # print(self.cost_list)

    def add_traffic(self, time):
        for key, value in self.adjacency_list.items():
            for node in value:
                traffic_factor = generate_traffic(time)
                if key not in self.traffic:
                    self.traffic[key] = {}
                self.traffic[key][node[0]] = traffic_factor

    def add_location(self, location_id, latitude, longitude):
        """
        Create Adjacency list of all edges
        :param location_id: Location_id of a location
        :param latitude: Latitude of the location
        :param longitude: Longitude of the location
        :return: None
        """
        self.adjacency_list[location_id] = []
        self.adjacency_list[location_id].extend([
            (connection.DestinationID_id, connection.Distance)
            for connection in Connections.objects.filter(SourceID_id=location_id)
        ])

    def add_cost_and_factor(self, source_id, destination_id, distance, time):
        """
        Find all paths to neighbour node along with route number, fare and time taken to reach the neighbour
        :param source_id: current node
        :param destination_id: neighbour node
        :param distance: distance between source and destination
        :param time: time of departure
        :return: None
        """

        route_fares = RouteDetails.objects.filter(
            RouteID__in=RouteDetails.objects.filter(StopID=source_id).values('RouteID'),
            StopID=destination_id
        ).select_related('RouteID').annotate(
            FarePerKM=F('RouteID__FarePerKM'),
            VehicleType=F('RouteID__VehicleType')
        ).values('RouteID', 'VehicleType', 'FarePerKM')

        # source_route_ids = RouteDetails.objects.filter(StopID=source_id).values_list('RouteID', flat=True)
        # destination_route_ids = RouteDetails.objects.filter(StopID=destination_id).values_list('RouteID', flat=True)
        #
        # # Find routes that are common to both source and destination and the stop sequences are consecutive
        # route_fares = RouteDetails.objects.filter(
        #     RouteID__in=source_route_ids.intersection(destination_route_ids),
        #     StopID=source_id,
        #     StopSequence=F('StopSequence') + 1
        # ).select_related('RouteID').annotate(
        #     FarePerKM=F('RouteID__FarePerKM'),
        #     VehicleType=F('RouteID__VehicleType')
        # ).values('RouteID', 'VehicleType', 'FarePerKM')

        # print("Source, Dest", source_id, destination_id)
        # print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        # print(route_fares)

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
                factor = decimal.Decimal(0.8) * fare + decimal.Decimal(0.2) * modified_time
                self.cost_list[source_id][destination_id].append((route_id, fare, modified_time, factor))
            else:
                factor = decimal.Decimal(0.8) * fare + decimal.Decimal(0.2) * usual_time
                self.cost_list[source_id][destination_id].append((route_id, fare, usual_time, factor))

    def calculate_best_path(self, source, destination, main_factor="Both"):
        """
        Calculate Best Path between source and destination using some factor
        :param source: Start node
        :param destination: Destination node
        :param main_factor: Calculate based on Fare, Time or Both
        :return: total fare, total time and path between source and destination
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
                print("Dijkstra returned")
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
