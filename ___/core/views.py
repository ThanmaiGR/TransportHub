import os
import datetime
from .functions import find_path, go_from_source_to_destination, str_to_time, Graph
from django.shortcuts import render, redirect, reverse
from .models import Locations, Routes
from django.contrib import messages
from django.utils import timezone
from django.utils.dateparse import parse_datetime
import numpy as np
import cv2
import pyautogui


def home(request):
    return render(
        request=request,
        template_name='core/home.html',
        context={}
    )


def main(request):
    locations = Locations.objects.values_list('LocationName', flat=True)
    if request.method == 'POST':
        source = Locations.objects.values_list('LocationID').filter(
            LocationName=request.POST.get('source')
        )[0][0]
        destination = Locations.objects.values_list('LocationID').filter(
            LocationName=request.POST.get('destination')
        )[0][0]
        time = parse_datetime(request.POST.get('time'))
        choice = request.POST.get('Choice')
        print('CHOICE:', choice)
        if not choice:
            choice = 'Both'
        if source == destination:
            messages.error(request, 'Source and Destination Cannot be Same')
        elif time.astimezone(datetime.timezone.utc) < timezone.now().replace(tzinfo=datetime.timezone.utc):
            messages.error(request, 'Please Enter a Valid Time')
        else:
            request.session['source'] = source
            request.session['destination'] = destination
            request.session['time'] = str(time)
            request.session['choice'] = choice
            return redirect(
                reverse('core:path')
            )
    return render(
        request=request,
        template_name='core/main.html',
        context={"locations": locations}
    )


def path(request):
    if request.method == 'POST':
        image = pyautogui.screenshot()
        image = cv2.cvtColor(
            np.array(image),
            cv2.COLOR_RGB2BGR
        )
        downloads_folder = os.path.join(os.getenv('USERPROFILE'), 'Downloads')
        cv2.imwrite(os.path.join(downloads_folder, "transport_routes.png"), image)

        return redirect(reverse('core:home'))
    source = request.session.get('source')
    destination = request.session.get('destination')
    time = parse_datetime(request.session.get('time'))
    choice = request.session.get('choice')
    g = Graph(time)
    total_fare, total_time, path_taken = g.calculate_best_path(source, destination, choice)

    if not request.session.get('source'):
        return redirect(reverse('core:main'))
    if path_taken:
        time_taken = str_to_time(total_time)
        actual_path = find_path(source, destination, path_taken)
        actual_path = go_from_source_to_destination(destination, source, actual_path)
        del request.session['source']
        del request.session['destination']

        for idx, row in enumerate(actual_path):
            start_id, stop_id, route_id, part_time = row[0], row[1], row[2], row[4]
            row[0] = Locations.objects.filter(LocationID=start_id).values_list(
                'LocationName',
                flat=True
            ).first()
            row[1] = Locations.objects.filter(LocationID=stop_id).values_list(
                'LocationName',
                flat=True
            ).first()
            row[2] = Routes.objects.filter(RouteID=route_id).values_list(
                'RouteName',
                flat=True
            ).first()
            row[4] = str_to_time(part_time)

        context = {
            "Fare": total_fare,
            "Time": time_taken,
            "Path": actual_path,
            "request": request
        }

        print("Fare ", total_fare)
        print("Time ", time_taken)
        print("Path ", actual_path)
    else:
        del request.session['source']
        del request.session['destination']
        del request.session['time']
        del request.session['choice']
        context = {"Distance": "No Route Found"}
    if request.user.is_authenticated:
        cab_fares = g.find_cabs(source, destination)
        context["cabs"] = cab_fares
    return render(
        request=request,
        template_name='core/path.html',
        context=context
    )
