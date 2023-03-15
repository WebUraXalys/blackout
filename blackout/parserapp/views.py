from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Streets, Buildings


@staff_member_required()
def fetch_cities(request):
    cities = Streets.objects.order_by('City').values('City').distinct()
    context = {'cities': cities}
    return render(request, 'parserapp/cities_list.html', context=context)


@staff_member_required()
def fetch_streets(request, city):
    streets = get_list_or_404(Streets, City=city)
    context = {'city': city,
               'streets': streets}
    return render(request, 'parserapp/streets_list.html', context=context)


@staff_member_required()
def delete_confirmation(request, **kwargs):
    """
    Method for confirming deleting objects. Kwargs contains city and street
    """
    try:
        street = kwargs['street']
    except:
        street = None
    context = {'city': kwargs['city'],
               'street': street}
    return render(request, 'parserapp/delete/delete_confirm.html', context=context)


@staff_member_required()
def delete_object(request, **kwargs):
    try:
        Streets.objects.get(City=kwargs['city'], Name=kwargs['street']).delete()  # Delete street
    except:
        Streets.objects.filter(City=kwargs['city']).delete()  # Delete city if kwargs['city'] is not defined
    return redirect('/cities/')


@staff_member_required()
def fetch_buildings(request, street, city):
    street_obj = get_object_or_404(Streets, Name=street, City=city)
    buildings = Buildings.objects.filter(Street=street_obj)
    context = {'city': city,
               'street': street,
               'buildings': buildings}
    return render(request, 'parserapp/buildings_list.html', context=context)
