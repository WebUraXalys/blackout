from rest_framework import generics, viewsets, status, serializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BuildingFilter
from .models import Buildings, Streets, Interruptions
from .serializers import BuildingSerializer, StreetSerializer, InterruptionSerializer


class BuildingList(generics.ListCreateAPIView):
    queryset = Buildings.objects.all()
    serializer_class = BuildingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BuildingFilter

    def perform_create(self, serializer):
        Street = get_object_or_404(Streets, Name=self.request.data.get('Street'))
        return serializer.save(Street=Street)


class BuildingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buildings.objects.all()
    serializer_class = BuildingSerializer
    lookup_field = 'id'


class StreetViewSet(viewsets.ModelViewSet):
    queryset = Streets.objects.all()
    serializer_class = StreetSerializer


class InterruptionViewSet(viewsets.ModelViewSet):
    queryset = Interruptions.objects.all()
    serializer_class = InterruptionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    