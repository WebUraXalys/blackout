import requests
import json
from django.http import JsonResponse
from ..models import Buildings


def send_buildings_coordinates():
    buildings = Buildings.objects.all
    data = []
    for building in buildings:
        longitude = building.Longitude
        latitude = building.Latitude

        data.append({latitude, longitude})

    response = requests.post("URL_апі", json=data)
    return JsonResponse(response.json())
