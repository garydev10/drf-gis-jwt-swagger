# from django.contrib import admin

# Register your models here.
from django.contrib.gis.db import models

class Location(models.Model):
    """
    A model which holds information about a particular location
    """
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    point = models.PointField(srid=4326)