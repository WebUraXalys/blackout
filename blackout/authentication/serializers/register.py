from user.serializers import UserSerializer
from user.models import User
from rest_framework import serializers
from rest_framework.validators import ValidationError
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(UserSerializer):
    password = serializers.CharField(
        required=True, write_only=True, validators=[validate_password]
    )
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password',
            'confirm_password',
            'first_name',
            'last_name',
            'icon',
        ]

        extra_kwargs = {
            'icon': {'required': False},
        }

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return User.objects.create_user(**validated_data)

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise ValidationError({'confirm_password': 'Passwords does not match'})
        return attrs
