import datetime
import random


class Graph:
    def __init__(self):
        # self.adjacency_list = {}
        # locations = Locations.objects.all()
        # for location in locations:
        #     self.add_location(location.LocationID, location.Latitude, location.Longitude)
        self.adjacency_list = self.ad_list()

    def add_location(self, location_id, latitude, longitude):
        self.adjacency_list[location_id] = []
        self.adjacency_list[location_id].extend([(connection.DestinationID_id, connection.Distance)
                                                 for connection in Connections.objects.filter(SourceID_id=location_id)])

    def ad_list(self):
        return {
            1: [(2, 5.0), (3, 3.0), (5, 15.0)],
            2: [(3, 12.0), (4, 7.0), (1, 5.0)],
            3: [(1, 3.0), (2, 12.0), (5, 14.0)],
            4: [(2, 7.0), (5, 2.5)],
            5: [(4, 2.5), (1, 15.0), (3, 14.0)],
        }

    def buses(self):


g = Graph()
# src, dest = map(int, input().split())
time = datetime.datetime.now()
print(g.adjacency_list)
base_time = datetime.time(00, 00, 00)
print(base_time)