from rest_framework import serializers

from .models import Aircraft, Airport,Airchart, Flight,Fly

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ('flight_id','flight_departureAirport','flight_arrivalAirport','flight_departureDate','flight_arrivalDate','flight_aircraft','flight_distance')

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ('airport_id','airport_name','airport_latitude','airport_longitude','airport_continent','airport_isoCountry','airport_isoRegion', 'airport_municipality')

class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ('aircraft_id','aircraft_model','aircraft_fClassSeats','aircraft_sClassSeats','aircraft_eClassSeats','aircraft_mileage','aircraft_maintenance','aircraft_maintenance_km','aircraft_staff','aircraft_status')