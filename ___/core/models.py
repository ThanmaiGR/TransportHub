from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Locations(BaseModel):
    LocationID = models.AutoField(primary_key=True)
    LocationName = models.CharField(max_length=255)
    Latitude = models.DecimalField(max_digits=10, decimal_places=8)
    Longitude = models.DecimalField(max_digits=11, decimal_places=8)

    class Meta:
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.LocationName


class Connections(BaseModel):
    SourceID = models.ForeignKey(Locations, on_delete=models.CASCADE,
                                 related_name='source', db_column="SourceID")
    DestinationID = models.ForeignKey(Locations, on_delete=models.CASCADE,
                                      related_name='destination', db_column="DestinationID")
    Distance = models.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        verbose_name_plural = 'Connections'


class Routes(BaseModel):
    RouteID = models.AutoField(primary_key=True)
    VehicleType = models.CharField(max_length=50)
    RouteName = models.CharField(max_length=255)
    FarePerKM = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Routes'

    def __str__(self):
        return self.RouteName


class CabCompanies(BaseModel):
    CompanyID = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Cab Companies'

    def __str__(self):
        return self.CompanyName


class CabFareStructure(BaseModel):
    CompanyID = models.OneToOneField(CabCompanies, on_delete=models.CASCADE,
                                     primary_key=True, db_column="CompanyID")
    BaseKM = models.DecimalField(max_digits=4, decimal_places=2)
    BasePrice = models.DecimalField(max_digits=10, decimal_places=2)
    PricePerKM = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Cab Fare Structures'


class Stops(BaseModel):
    StopID = models.IntegerField(primary_key=True)
    StopName = models.CharField(max_length=250)
    LocationID = models.ForeignKey(Locations, on_delete=models.CASCADE, db_column="Location")

    class Meta:
        verbose_name_plural = 'Stops'


class RouteDetails(BaseModel):
    RouteID = models.ForeignKey(Routes, on_delete=models.CASCADE, db_column="RouteID")
    StopSequence = models.IntegerField()
    StopID = models.ForeignKey(Stops, on_delete=models.CASCADE, db_column="StopID")

    class Meta:
        unique_together = ('RouteID', 'StopSequence')
        verbose_name_plural = 'Route Details'


# class Schedules(BaseModel):
#     ScheduleID = models.AutoField(primary_key=True)
#     RouteID = models.ForeignKey(Routes, on_delete=models.CASCADE, db_column="RouteID")
#     DepartureTime = models.TimeField()


# class CabBookings(BaseModel):
#     BookingID = models.AutoField(primary_key=True)
#     UserID = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     CompanyID = models.ForeignKey(CabCompanies, on_delete=models.CASCADE, )
#     SourceLocationID = models.ForeignKey(Locations, on_delete=models.CASCADE, related_name='source_location')
#     DestinationLocationID = models.ForeignKey(Locations, on_delete=models.CASCADE,
#     related_name='destination_location')
#     BookingTime = models.DateTimeField()
#
#     def __str__(self):
#         return f"Booking {self.BookingID} - {self.UserID}"
