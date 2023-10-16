from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .viewsets.register import RegisterViewSet

router = SimpleRouter()
router.register('register', RegisterViewSet, 'register')

urlpatterns = [
    path('', include(router.urls)),
]
