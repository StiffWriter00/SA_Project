# Generated by Django 4.0.4 on 2022-04-27 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('aircraft_id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('aircraft_model', models.CharField(max_length=256)),
                ('f_class_seats', models.IntegerField(default=0)),
                ('s_class_seats', models.IntegerField(default=0)),
                ('e_class_seats', models.IntegerField(default=0)),
                ('aircraft_mileage', models.IntegerField(default=0)),
                ('aircraft_maintenance', models.DateField(blank=True, null=True)),
                ('aircraft_maintenance_km', models.IntegerField(default=0)),
                ('aircraft_staff', models.IntegerField(default=0)),
                ('aircraft_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport_id', models.CharField(max_length=16)),
                ('airport_name', models.CharField(max_length=256)),
                ('airport_latitude', models.IntegerField(default=0)),
                ('airport_longitude', models.IntegerField(default=0)),
            ],
        ),
    ]
