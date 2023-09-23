from rest_framework import serializers
from .models import Cards

class CardsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cards
        exclude = ('Owner',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['Location'] = instance.Location.Name
        data['Building'] = instance.Building.Address
        data['Owner'] = instance.Owner.username
        return data

    def create(self,validated_data):
        validated_data['Owner'] = self.context['request'].user
        obj = Cards.objects.create(**validated_data)
        return obj
