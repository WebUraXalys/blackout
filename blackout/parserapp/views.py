#from .services.parser import start_browser, get_page

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Streets

def start(request):
    data = [
        {'name': 'Arhypenka', 'city': 'Lviv', 'otg': 'Lvivska', 'region': 'Lvivskyi'},
        {'name': 'Tarnavskogo', 'city': 'Lviv', 'otg': 'Lvivska', 'region': 'Lvivskyi'},
        {'name': 'Stryiska', 'city': 'Lviv', 'otg': 'Lvivska', 'region': 'Lvivskyi'},
    ]

    for item in data:
        street = Streets.objects.create(
            Name=item['name'], City=item['city'], OTG=item['otg'], Region=item['region']
        )

        print(street.Name, street.City, street.OTG, street.Region)

    return render(request, 'templates/data_list.html', {'data': data})

#start(request=HttpResponse)