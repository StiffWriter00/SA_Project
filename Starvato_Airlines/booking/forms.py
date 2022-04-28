from django import forms
from requests import request
from .models import Flight


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['flight_departureAirport' , 'flight_arrivalAirport', 'flight_departureDate',]