from django.urls import path
from .views import BuildingList, CoordinatesApiView

urlpatterns = [
    path('buildings/', BuildingList.as_view()),
    path('coordinates/', CoordinatesApiView.as_view())
]
