from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.text import slugify
from .models import Streets, Buildings


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
