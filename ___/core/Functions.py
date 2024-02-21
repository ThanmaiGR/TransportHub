from .models import Locations, Connections, Routes, Stops, RouteDetails, Schedules
from decimal import Decimal
from django.db.models import F
from django.db.models import Max
from django.db.models import Min
import heapq


def get_info(src, dest, time, farefact = 0.8):
    graph = []
    graph_objects = Connections.objects.values_list('SourceID', 'DestinationID', 'Distance')
    for each in graph_objects:
        graph.append(each)
    # print(graph)
    route_objects = Routes.objects.values_list('RouteID', 'VehicleType', 'FarePerKM')
    routes = []
    for each in route_objects:
        routes.append(each)
    # print(routes)
    stops = []
    stop_objects = Stops.objects.values_list('StopID', 'LocationID')
    for each in stop_objects:
        stops.append(each)
    # print(stops)






    queryset = RouteDetails.objects.annotate(
        route_id=F('RouteID'),
        stop_id=F('StopID'),
        stop_sequence=F('StopSequence'),
    ).values('route_id', 'stop_id', 'stop_sequence')

    # Grouping by RouteID
    queryset = queryset.annotate(
        min_sequence=Min('stop_sequence')
    ).order_by('min_sequence')

    # Execute the query
    result = list(queryset)
    print(result)


def shortest_path(self, src):
    # Create a priority queue to store vertices that
    # are being preprocessed.
    pq = [(0, src)]  # The first element of the tuple is the distance, and the second is the vertex label

    # Create a list for distances and initialize all
    # distances as infinite (INF)
    dist = [float('inf')] * self.V
    dist[src] = 0

    # Looping until the priority queue becomes empty
    while pq:
        # The first element in the tuple is the minimum distance vertex
        # Extract it from the priority queue
        current_dist, u = heapq.heappop(pq)

        # Iterate over all adjacent vertices of a vertex
        for v, weight in self.adj[u]:
            # If there is a shorter path to v through u
            if dist[v] > dist[u] + weight:
                # Update the distance of v
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    # Print shortest distances
    print("Vertex Distance from Source")
    for i in range(self.V):
        print(f"{i}\t\t{dist[i]}")