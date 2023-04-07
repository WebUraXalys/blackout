from rest_framework import serializers
from .models import Buildings, Interruptions, Streets


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Streets
        fields = ['Name', 'City', 'OTG', 'Region']


class InterruptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interruptions
        fields = ['Start', 'End', 'Type']


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buildings
        fields = ['Address', 'Street', 'Group', 'Interruption', 'Longitude', 'Latitude']
