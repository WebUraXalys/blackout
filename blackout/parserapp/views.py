from datetime import datetime
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from fuzzywuzzy import fuzz
from .filters import BuildingFilter
from .models import Buildings, Streets, Interruptions
from .serializers import BuildingSerializer, StreetSerializer, InterruptionSerializer, CoordinatesSerializer


class BuildingList(generics.ListCreateAPIView):
    queryset = Buildings.objects.all()
    serializer_class = BuildingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BuildingFilter

    def perform_create(self, serializer):
        for street in Streets.objects.all():
            if fuzz.partial_ratio(street.Name, self.request.data.get('Street')) > 70:
                Street = get_object_or_404(Streets, Name=street.Name)
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


class CoordinatesApiView(generics.ListAPIView):
    queryset = Buildings.objects.all()
    serializer_class = CoordinatesSerializer

    def list(self, request):
        coordinates = []
        authenticated = request.user.is_authenticated

        if authenticated:
            streets = Streets.objects.all()
        else:
            streets = Streets.objects.filter(City__icontains='Львів')

        for street in streets:
            builds_of_street = Buildings.objects.filter(Street=street, Interruption__End__gte=datetime.now())
            for build in builds_of_street:
                if build.Longitude or build.Latitude:
                    coordinates.append((float(build.Longitude), float(build.Latitude)))

        if coordinates:
            return Response({'message': 'ok', 'Coordinates': coordinates})
        else:
            message = 'No coordinates available.'
            return Response({'message': message})
