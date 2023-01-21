from django.contrib import admin

from parserapp.models import Streets, Buildings, Interruptions


@admin.register(Streets)
class StreetsAdmin(admin.ModelAdmin):
    list_display = ['pk','Name', 'City', 'OTG','Region']
    ordering = ['Name']

@admin.register(Buildings)
class BuildingsAdmin(admin.ModelAdmin):
    list_display = ['pk','Address', 'Street', 'Group','Interruption','get_type_interruption','Longitude','Latitude']
    ordering = ['pk']

    def get_type_interruption(self, obj):
        if obj.Interruption:
            return obj.Interruption.Type
    
    
    
    get_type_interruption.short_description = 'Type Interruption'

@admin.register(Interruptions)
class InterruptionAdmin(admin.ModelAdmin):
    list_display = ['pk','Start', 'End', 'Type']
    ordering = ['pk']






