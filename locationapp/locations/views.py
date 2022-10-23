# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework_gis.filters import DistanceToPointFilter
from .models import Location
from .serializers import LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    distance_filter_field = 'geometry'
    filter_backends = (DistanceToPointFilter,)
    bbox_filter_include_overlapping = True