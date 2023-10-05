from user.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.serializers import ValidationError


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True, validators=[validate_password])
    password2 = serializers.CharField(required=True, write_only=True)
    email = serializers.CharField(required=True, validators=[validate_email])

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError({'password': 'Password does not match'})

        if User.objects.filter(email=attrs['email']).exists():
            raise ValidationError({'email': 'Email already exist'})

        return attrs

    def create(self, validated_data):
        user = User(username=validated_data['username'], email=self.validated_data['email'])

        user.set_password(validated_data['password'])
        user.save()

        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True, validators=[validate_password])
    password2 = serializers.CharField(
        required=True,
        write_only=True,
    )
    old_password = serializers.CharField(
        required=True,
        write_only=True,
    )

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError({'password': 'Password does not match'})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user

        if not user.check_password(value):
            raise ValidationError('Old password is not correct')

        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'last_login')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'username': {'required': False},
            'last_login': {'read_only': True},
        }

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({'email': 'This email is already in use.'})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({'username': 'This username is already in use.'})
        return value
