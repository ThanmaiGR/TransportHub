from django.db import models


class Locations(models.Model):
    LocationID = models.AutoField(primary_key=True)
    LocationName = models.CharField(max_length=255)
    Latitude = models.DecimalField(max_digits=10, decimal_places=8)
    Longitude = models.DecimalField(max_digits=11, decimal_places=8)

    def __str__(self):
        return self.LocationName


class Connections(models.Model):
    SourceID = models.ForeignKey(Locations, on_delete=models.CASCADE,
                                 related_name='source', db_column="SourceID")
    DestinationID = models.ForeignKey(Locations, on_delete=models.CASCADE,
                                      related_name='destination', db_column="DestinationID")
    Distance = models.DecimalField(max_digits=3, decimal_places=1)


class Routes(models.Model):
    RouteID = models.AutoField(primary_key=True)
    VehicleType = models.CharField(max_length=50)
    RouteName = models.CharField(max_length=255)
    FarePerKM = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.RouteName


class CabCompanies(models.Model):
    CompanyID = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=255)

    def __str__(self):
        return self.CompanyName


class CabFareStructure(models.Model):
    CompanyID = models.OneToOneField(CabCompanies, on_delete=models.CASCADE,
                                     primary_key=True, db_column="CompanyID")
    BasePrice = models.DecimalField(max_digits=10, decimal_places=2)
    PricePerKM = models.DecimalField(max_digits=5, decimal_places=2)


class Stops(models.Model):
    StopID = models.IntegerField(primary_key=True)
    StopName = models.CharField(max_length=250)
    LocationID = models.ForeignKey(Locations, on_delete=models.CASCADE, db_column="Location")


class RouteDetails(models.Model):
    RouteID = models.ForeignKey(Routes, on_delete=models.CASCADE, db_column="RouteID")
    StopSequence = models.IntegerField()
    StopID = models.ForeignKey(Stops, on_delete=models.CASCADE, db_column="StopID")
    ArrivalTime = models.TimeField()

    class Meta:
        unique_together = ('RouteID', 'StopSequence')


class Schedules(models.Model):
    ScheduleID = models.AutoField(primary_key=True)
    RouteID = models.ForeignKey(Routes, on_delete=models.CASCADE, db_column="RouteID")
    DepartureTime = models.TimeField()




# class CabBookings(models.Model):
#     BookingID = models.AutoField(primary_key=True)
#     UserID = models.ForeignKey('auth.User', on_delete=models.CASCADE)
# Assuming you use Django's built-in User model
#     CompanyID = models.ForeignKey(CabCompanies, on_delete=models.CASCADE, )
#     SourceLocationID = models.ForeignKey(Locations, on_delete=models.CASCADE, related_name='source_location')
#     DestinationLocationID = models.ForeignKey(Locations, on_delete=models.CASCADE,
#     related_name='destination_location')
#     BookingTime = models.DateTimeField()
#
#     def __str__(self):
#         return f"Booking {self.BookingID} - {self.UserID}"
