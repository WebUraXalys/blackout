from django.contrib import admin

from parserapp.models import Streets, Buildings, Interruptions


@admin.register(Streets)
class StreetsAdmin(admin.ModelAdmin):
    list_display = ['pk','Name', 'City', 'OTG','Region']
    ordering = ['Name']

@admin.register(Buildings)
class StreetsAdmin(admin.ModelAdmin):
    list_display = ['pk','Address', 'Street', 'Group','Interruption']
    ordering = ['Address']

@admin.register(Interruptions)
class InterruptionAdmin(admin.ModelAdmin):
    list_display = ['pk','Start', 'End', 'Type']
    ordering = ['pk']






