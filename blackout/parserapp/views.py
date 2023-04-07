from rest_framework import generics
from .models import Buildings
from .serializers import BuildingSerializer


class BuildingList(generics.ListCreateAPIView):
    queryset = Buildings.objects.all()
    serializer_class = BuildingSerializer


class BuildingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buildings.objects.all()
    serializer_class = BuildingSerializer
    lookup_field = 'id'
