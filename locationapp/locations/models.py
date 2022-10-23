# from django.db import models

# Create your models here.
from django.contrib.gis.db import models

class Location(models.Model):
    """
    A model which holds information about a particular location
    """
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    location = models.PointField(srid=4326)
   
    def __str__(self):
        return self.name