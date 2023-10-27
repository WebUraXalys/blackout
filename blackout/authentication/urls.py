from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .viewsets.register import RegisterViewSet
from .viewsets.login import LoginViewSet


router = SimpleRouter()
router.register('register', RegisterViewSet, 'register')
router.register('login', LoginViewSet, 'login')

urlpatterns = [
    path('', include(router.urls)),
]
