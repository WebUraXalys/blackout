from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True, read_only=True)

    class Meta:
        model = User

        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'updated',
            'created',
            'is_active',
        ]

        read_only_fields = [
            'updated',
            'created',
        ]
