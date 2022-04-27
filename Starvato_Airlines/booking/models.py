from django.db import models

# Create your models here.
class Aircraft(models.Model):
    aircraft_id = models.CharField(max_length=16, primary_key=True)
    aircraft_model = models.CharField(max_length=256)
    aircraft_fClassSeats = models.IntegerField(default=0)
    aircraft_sClassSeats = models.IntegerField(default=0)
    aircraft_eClassSeats = models.IntegerField(default=0)
    aircraft_mileage = models.IntegerField(default=0)
    aircraft_maintenance = models.DateField(blank=True,null=True)
    aircraft_maintenance_km = models.IntegerField(default=0)
    aircraft_staff = models.IntegerField(default=0)
    aircraft_status = models.BooleanField(default=True)

class Airport(models.Model):
    airport_id = models.CharField(max_length=16, primary_key=True)
    airport_name = models.CharField(max_length=256)
    airport_latitude = models.IntegerField(default=0)
    airport_longitude = models.IntegerField(default=0)
    airport_continent = models.CharField(max_length=256)
    airport_isoCountry = models.IntegerField(default=0)
    airport_isoRegion = models.IntegerField(default=0)
    airport_municipality = models.CharField(max_length=10)

class Flight(models.Model):
    flight_id = models.CharField(max_length=16, primary_key=True)
    flight_departureAirport = models.ForeignKey(Airport,on_delete=models.SET_NULL,null=True,related_name='ad')
    flight_arrivalAirport = models.ForeignKey(Airport,on_delete=models.SET_NULL,null=True,related_name='aa')
    flight_departureDate = models.DateField(blank=True,null=True)
    flight_arrivalDate = models.DateField(blank=True,null=True)
    flight_aircraft = models.ForeignKey(Aircraft,on_delete=models.SET_NULL,null=True)
    flight_distance = models.IntegerField(default=0)