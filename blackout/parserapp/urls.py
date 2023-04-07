from django.urls import path
from .views import BuildingList, BuildingDetail

urlpatterns = [path('buildings/', BuildingList.as_view()),
                path('buildings/<int:id>/', BuildingDetail.as_view())]
