from django.shortcuts import render
from .models import Flight
from rest_framework import viewsets
# Create your views here.
class booking(viewsets.ModelViewSet):
    queryset = Flight.objects.all().order_by('flight_id')


def home_view(request):
    return render(request, 'index.html', {})