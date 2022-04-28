from django.shortcuts import render
from .models import Flight, Airport
from rest_framework import viewsets
# Create your views here.
class booking(viewsets.ModelViewSet):
    queryset = Flight.objects.all().order_by('flight_id')


def home_view(request):
    return render(request, 'index.html', {})

def airport_view(request):
    airport_departure = request.POST.get('airport_departure', '')
    airport_arrival = request.POST.get('airport_arrival', '')
    airport_dep = Airport.objects.get(airport_name = airport_departure)
    airport_arr = Airport.objects.get(airport_name = airport_arrival)

def flight_view(request):
    date_departure = request.POST.get('date_departure', '')
    date_arrival = request.POST.get('date_arrival', '')
    airport_dep = Airport.objects.get(airport_name = airport_departure)
    airport_arr = Airport.objects.get(airport_name = airport_arrival)