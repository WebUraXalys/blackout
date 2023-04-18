from rest_framework import generics
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BuildingFilter
from .models import Buildings, Streets
from .serializers import BuildingSerializer


class BuildingList(generics.ListCreateAPIView):
    queryset = Buildings.objects.all()
    serializer_class = BuildingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BuildingFilter

    def perform_create(self, serializer):
        Street = get_object_or_404(Streets, Name = self.request.data.get('Street'))
        return serializer.save(Street=Street)


class BuildingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buildings.objects.all()
    serializer_class = BuildingSerializer
    lookup_field = 'id'


