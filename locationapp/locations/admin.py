# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import Location

class LocationAdmin(GISModelAdmin):
    list_display = ('name', 'address', 'country')
    list_editable = ('address', 'country')
    # default location London
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 11,
            'default_lon': -0.127758,
            'default_lat': 51.507351,
        },
    }

admin.site.register(Location, LocationAdmin)