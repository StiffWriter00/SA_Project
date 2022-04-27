from django.contrib import admin
from .models import Aircraft, Airport, Flight
# Register your models here.
admin.site.register([Aircraft, Airport, Flight])