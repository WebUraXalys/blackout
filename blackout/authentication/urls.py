from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterApiView, MyTokenObtainPairView


urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name ='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name ='refresh'),
    path('register/', RegisterApiView.as_view(), name='register'),
]