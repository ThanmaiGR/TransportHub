import datetime
from .Functions import get_info
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Locations, Connections
from django.contrib import messages
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.http import HttpResponse, HttpResponseRedirect
from .testcalc import Graph
# Create your views here.


def home(request):
    return render(request=request,
                  template_name='core/home.html',
                  context={})


def main(request):
    locations = Locations.objects.values_list('LocationName', flat=True)
    if request.method == 'POST':
        source = Locations.objects.values_list('LocationID').filter(LocationName=request.POST.get('source'))[0][0]
        print(source)
        # destination = request.POST.get('destination')
        destination = Locations.objects.values_list('LocationID').filter(
            LocationName=request.POST.get('destination'))[0][0]
        time = parse_datetime(request.POST.get('time'))
        pretime = request.POST.get('pretime')
        prefare = float(request.POST.get('prefare'))
        if source == destination:
            messages.error(request, 'Cmon bruh Walk')
        elif time.replace(tzinfo=datetime.timezone.utc) < timezone.now().replace(tzinfo=datetime.timezone.utc):
            messages.error(request, 'Time Machine Not Created Yet')
        else:
            # get_info(source, destination, time)
            g = Graph()
            distance = g.calculate_shortest_path(source, destination, prefare)
            dist = Connections.objects.values_list('Distance')
            for each in dist:
                print(each)
            context = {"Distance": distance}
            if distance == float('inf'):
                context = {"Distance":"No Route Found"}
            return render(request=request,
                          template_name='core/path.html',
                          context=context)
    return render(request=request,
                  template_name='core/main.html',
                  context={"locations": locations})


def path(request):
    pass
