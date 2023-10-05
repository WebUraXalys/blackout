from django.contrib import admin
from .models import Cards


@admin.register(Cards)
class BuildingsAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'Title',
        'Icon',
        'Owner',
        'get_city',
        'get_street',
        'Building',
    ]
    ordering = ['pk']

    def get_city(self, obj):
        if obj.Location:
            return obj.Location.City
        return None

    def get_street(self, obj):
        if obj.Location:
            return obj.Location.Name
        return None

    get_city.short_description = 'City'
    get_street.short_description = 'Street'
