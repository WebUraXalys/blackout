from parserapp.services.parser import parsing_process
# Create your views here.

from django.http import HttpResponse


def start(request):
    x = parsing_process()
    return HttpResponse(x)
