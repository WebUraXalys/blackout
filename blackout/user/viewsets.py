from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['patch', 'get', 'post']
    permission_classes = [
        AllowAny,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        obj = User.objects.get(pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)
