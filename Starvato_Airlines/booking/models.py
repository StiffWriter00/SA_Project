from django.db import models

# Create your models here.
class Aircraft(models.Model):
    aircraft_id = models.CharField(max_length=16, primary_key=True)
    aircraft_model = models.CharField(max_length=256)
    aircraft_fClassSeats = models.IntegerField(default=0)
    aircraft_sClassSeats = models.IntegerField(default=0)
    aircraft_eClassSeats = models.IntegerField(default=0)
    aircraft_mileage = models.IntegerField(default=0)
    aircraft_maintenanceDate = models.DateField(blank=True,null=True)
    aircraft_maintenanceKm = models.IntegerField(default=0)
    aircraft_staff = models.IntegerField(default=0)
    aircraft_status = models.BooleanField(default=True)

    def __str__(self):
        return self.aircraft_model

class Airport(models.Model):
    airport_id = models.CharField(max_length=16, primary_key=True)
    airport_name = models.CharField(max_length=256)
    airport_latitude = models.IntegerField(default=0)
    airport_longitude = models.IntegerField(default=0)
    airport_continent = models.CharField(max_length=256)
    airport_isoCountry = models.IntegerField(default=0)
    airport_isoRegion = models.IntegerField(default=0)
    airport_municipality = models.CharField(max_length=10)

    def __str__(self):
        return self.airport_name

class Flight(models.Model):
    flight_id = models.CharField(max_length=16, primary_key=True)
    flight_departureAirport = models.ForeignKey(Airport,on_delete=models.SET_NULL,null=True,related_name='ad')
    flight_arrivalAirport = models.ForeignKey(Airport,on_delete=models.SET_NULL,null=True,related_name='aa')
    flight_departureDate = models.DateField(blank=True,null=True)
    flight_arrivalDate = models.DateField(blank=True,null=True)
    flight_aircraft = models.ForeignKey(Aircraft,on_delete=models.SET_NULL,null=True)
    flight_distance = models.IntegerField(default=0)

    def __str__(self):
        return str(self.flight_arrivalAirport) + ' ' + str(self.flight_departureDate)