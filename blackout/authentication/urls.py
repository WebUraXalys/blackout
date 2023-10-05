from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterApiView, MyTokenObtainPairView, ChangePasswordApiView, UpdateProfileApiView
from authentication.views import APILogoutView

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('register/', RegisterApiView.as_view(), name='register'),
    path('user/change-password/', ChangePasswordApiView.as_view(), name='change_password'),
    path('user/profile/', UpdateProfileApiView.as_view(), name='profile'),
    path('logout/', APILogoutView.as_view(), name='logout'),
]
