from rest_framework import serializers
from .models import Buildings, Interruptions, Streets


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Streets
        fields = ['Name', 'City', 'OTG', 'Region']


class InterruptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interruptions
        fields = ['id', 'Start', 'End', 'Type']

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

    def to_representation(self, instance):
        representation = super(BuildingSerializer, self).to_representation(instance)
        Interruption = Interruptions.objects.filter(id = representation['Interruption']).first()
        if Interruption:
            representation['Interruption'] = {
                'id': Interruption.id,
                'Start': Interruption.Start.strftime('%d/%m/%Y %H:%M:%S'),
                'End': Interruption.End.strftime('%d/%m/%Y %H:%M:%S'),
                'Type': Interruption.Type,

            }
        return representation


class CoordinatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Buildings
        fields = ['Longitude', 'Latitude']
