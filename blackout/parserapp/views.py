from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Streets, Buildings


@staff_member_required()
def start(request):
    cities = Streets.objects.order_by('City').values('City').distinct()
    context = {'cities': cities}
    return render(request, 'parserapp/city.html', context=context)


@staff_member_required()
def city_view(request, city):
    streets = Streets.objects.filter(City=city).order_by('Name')
    context = {'city': city,
               'streets': streets}
    return render(request, 'parserapp/streets.html', context=context)


@staff_member_required()
def predelete_view(request, **kwargs):
    """
    Method for confirming deleting objects. Kwargs gets city and street
    """
    try:
        street = kwargs['street']
    except:
        street = None
    context = {'city': kwargs['city'],
               'street': street}

    return render(request, 'parserapp/delete/predelete.html', context=context)


@staff_member_required()
def delete_view(request, **kwargs):
    try:
        Streets.objects.get(City=kwargs['city'], Name=kwargs['street']).delete()  # Delete street
    except:
        Streets.objects.filter(City=kwargs['city']).delete()  # Delete city if kwargs['city'] is not defined
    return redirect('/parser/')


@staff_member_required()
def streets_view(request, street, city):
    street_obj = Streets.objects.get(Name=street, City=city)
    buildings = Buildings.objects.filter(Street=street_obj)
    context = {'city': city,
               'street': street,
               'buildings': buildings}
    return render(request, 'parserapp/buildings.html', context=context)
