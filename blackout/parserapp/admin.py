from django.contrib import admin

from parserapp.models import Street, Building, Region

@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ['pk','name', 'city', 'OTG',"region"]
    ordering = ['pk']

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ['pk','address', 'street', 'group']



@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['pk','name']
    ordering = ['pk']

