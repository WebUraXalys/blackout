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

    def validate(self, attrs):
        start_date = attrs.get('Start')
        end_date = attrs.get('End')

        if None in [start_date,end_date]:
            raise serializers.ValidationError('Value field cannot be empty.')

        return attrs


class BuildingSerializer(serializers.ModelSerializer):
    Street = serializers.CharField()

    class Meta:
        model = Buildings
        fields = ['Address', 'Street', 'Group', 'Interruption', 'Longitude', 'Latitude']
