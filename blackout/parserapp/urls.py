from django.urls import path
from .views import *

urlpatterns = [
    path("", fetch_cities, name="cities"),
    path("<city_slug>/", fetch_streets, name="city"),
    path("confirm/<city_slug>/", delete_confirmation, name="delete-confirm-city"),
    path("confirm/<city_slug>/<street_slug>/", delete_confirmation, name="delete-confirm-street"),
    path("delete/<city_slug>/", delete_object, name="delete-city"),
    path("delete/<city_slug>/<street_slug>/", delete_object, name="delete-street"),
    path("<city_slug>/<street_slug>/", fetch_buildings, name="street"),
]
