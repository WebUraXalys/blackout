from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers



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
        fields = ['username', 'email', 'password', 'password2' ]


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Password does not match'})

        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email': 'Email already exist'})


        return attrs

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email = self.validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

