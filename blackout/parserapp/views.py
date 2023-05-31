from datetime import datetime
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.text import slugify
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
            if fuzz.partial_ratio(street.Name, self.request.data.get('Street'))>70:
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


@staff_member_required()
def fetch_cities(request):
    data = []
    cities = Streets.objects.order_by('City').values('City').distinct()
    # Get slug for city and pack it into one dictionary. Then it append to context data
    for city in cities:
        slug = Streets.objects.get(City=city['City']).Slug_city
        data.append({'city': city, 'slug': slug})
    context = {'data': data}
    return render(request, 'parserapp/cities_list.html', context=context)

 
@staff_member_required()
def fetch_streets(request, city_slug):
    streets = get_list_or_404(Streets, Slug_city=city_slug)
    city = Streets.objects.get(Slug_city=city_slug).City
    context = {'city_slug': city_slug,
               'city': city,
               'streets': streets}
    return render(request, 'parserapp/streets_list.html', context=context)


@staff_member_required()
def delete_confirmation(request, city_slug, street_slug = None):
    """
    Method for confirming deleting objects. Kwargs contains city and street
    """
    street = None
    try:
        street = Streets.objects.get(Slug_city=city_slug, Slug_name=street_slug).Name
    except:
        city = Streets.objects.get(Slug_city=city_slug).City
    context = {'city': city,
               'street': street,
               'city_slug': city_slug,
               'street_slug': street_slug}
    return render(request, 'parserapp/delete/delete_confirm.html', context=context)


@staff_member_required()
def delete_object(request, **kwargs):
    try:
        Streets.objects.get(Slug_city=kwargs['city_slug'], Slug_name=kwargs['street_slig']).delete()  # Delete street
    except:
        Streets.objects.filter(Slug_city=kwargs['city_slug']).delete()  # Delete city if kwargs['street_slug'] is not defined
    return redirect('/cities/')


@staff_member_required()
def fetch_buildings(request, street_slug, city_slug):
    street_obj = get_object_or_404(Streets, Slug_street=street_slug, Slug_city=city_slug)
    buildings = Buildings.objects.filter(Street=street_obj)
    context = {'city_slug': city_slug,
               'street_slug': street_slug,
               'street': street_obj,
               'buildings': buildings}
    return render(request, 'parserapp/buildings_list.html', context=context)
