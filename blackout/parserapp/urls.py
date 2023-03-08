from django.urls import path
from .views import *

urlpatterns = [
    path("", start, name="start"),
    path("<city>/", city_view, name="city"),
    path("predelete/<city>/", predelete_view, name="delete"),
    path("predelete/<city>/<street>/", predelete_view, name="delete-street"),
    path("delete/<city>/", delete_view, name="confirm-delete-city"),
    path("delete/<city>/<street>/", delete_view, name="confirm-delete-street"),
    path("<city>/<street>/", streets_view, name="street")
]
