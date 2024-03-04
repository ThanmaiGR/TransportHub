from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Locations)
admin.site.register(Connections)
admin.site.register(CabCompanies)
admin.site.register(CabFareStructure)
admin.site.register(Routes)
admin.site.register(RouteDetails)
admin.site.register(Stops)
