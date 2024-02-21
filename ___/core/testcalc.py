import heapq

from django.db.models import F

from .models import Locations, Routes, Connections, RouteDetails


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.cost_list = {}
        self.time_list = {}
        locations = Locations.objects.all()
        for location in locations:
            self.add_location(location.LocationID, location.Latitude, location.Longitude)
        edges = Connections.objects.all()

        for edge in edges:
            print("EDGE:", edge.SourceID_id, edge.DestinationID_id, edge.Distance)
            self.add_cost(edge.SourceID_id, edge.DestinationID_id, edge.Distance)
        print("Distances")
        for key, value in self.cost_list.items():
            print(key, value)
        print("End")

    def add_location(self, location_id, latitude, longitude):
        self.adjacency_list[location_id] = []
        self.adjacency_list[location_id].extend([(connection.DestinationID_id, connection.Distance)
                                                 for connection in Connections.objects.filter(SourceID_id=location_id)])

    def add_cost(self, source_id, destination_id, distance):
        src_node_details = RouteDetails.objects.filter(StopID=source_id)
        dest_node_details = RouteDetails.objects.filter(StopID=destination_id)
        routes = Routes.objects.all()

        route_fares  = RouteDetails.objects.filter(
            RouteID__in=RouteDetails.objects.filter(StopID=source_id).values('RouteID'),
            StopID=destination_id
        ).annotate(
            FarePerKM=F('RouteID__FarePerKM')
        ).values('RouteID', 'FarePerKM')
        if source_id not in self.cost_list:
            self.cost_list[source_id] = {}
        self.cost_list[source_id][destination_id] = []

        for each_fare in route_fares:
            fare = each_fare['FarePerKM'] * distance
            route_id = each_fare['RouteID']
            self.cost_list[source_id][destination_id].append((route_id, fare))

    def calculate_shortest_path(self, src, dest, max_fare=1000):
        for key, each in self.adjacency_list.items():
            print(key, each)
        pq = [(0, src)]  # The first element is the total fare, the second is the location id

        total_fare = {location_id: float('inf') for location_id in self.adjacency_list}
        total_fare[src] = 0

        while pq:
            current_fare, current_location_id = heapq.heappop(pq)

            if current_fare > max_fare:
                continue

            if current_location_id == dest:
                return total_fare[dest][src]

            for neighbor_id, distance in self.adjacency_list[current_location_id]:
                new_fare = current_fare + distance * Routes.objects.get(RouteID=neighbor_id).FarePerKM
                if new_fare < total_fare[neighbor_id]:
                    total_fare[neighbor_id] = new_fare
                    heapq.heappush(pq, (new_fare, neighbor_id))

        for fare in total_fare:
            print(fare)
        return float('inf'), total_fare
