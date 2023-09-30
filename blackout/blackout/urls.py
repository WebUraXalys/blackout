from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter
from parserapp.views import StreetViewSet, InterruptionViewSet
from user.viewsets import UserViewSet


router = SimpleRouter(trailing_slash=False)
router.register('streets', StreetViewSet, basename='streets')
router.register('interruptions', InterruptionViewSet, basename='interruptions')
router.register('user/?', UserViewSet, basename='user')


urlpatterns = [
    # path('api/', include('parserapp.urls',)),
    path('auth/', include('authentication.urls')),
    path('api/', include(router.urls)),
    path('accounts/login/', RedirectView.as_view(permanent=False, url='/admin/')),
    path(
        'admin/password_reset/',
        auth_views.PasswordResetView.as_view(),
        name='admin_password_reset',
    ),
    path(
        'admin/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
    path('admin/', admin.site.urls),
    path('cities/', include('parserapp.urls')),
    path('api/', include('cards.urls'))
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)