from django.urls import path
from .views import *

urlpatterns = [
    path("", fetch_cities, name="cities"),
    path("<city>/", fetch_streets, name="city"),
    path("confirm/<city>/", delete_confirmation, name="delete-confirm-city"),
    path("confirm/<city>/<street>/", delete_confirmation, name="delete-confirm-street"),
    path("delete/<city>/", delete_object, name="delete-city"),
    path("delete/<city>/<street>/", delete_object, name="delete-street"),
    path("<city>/<street>/", fetch_buildings, name="street")
]
