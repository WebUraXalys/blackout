from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from parserapp.views import  StreetViewSet, InterruptionViewSet

router = DefaultRouter()
router.register('streets', StreetViewSet, basename='streets')
router.register('interruptions', InterruptionViewSet, basename='interruptions')


urlpatterns = [
    path('api/', include('parserapp.urls',)),
    path('auth/', include('authentication.urls')),
    path('api/', include(router.urls)),

    path('accounts/login/', RedirectView.as_view(permanent=False, url='/admin/')),
    path(
        "admin/password_reset/",
        auth_views.PasswordResetView.as_view(),
        name="admin_password_reset",
    ),
    path(
        "admin/password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("admin/", admin.site.urls),
    path("cities/", include("parserapp.urls")),
]
