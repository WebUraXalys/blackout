from django.urls import path
from .views import BuildingList

urlpatterns = [
    path('buildings/', BuildingList.as_view()),
]
