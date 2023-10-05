import email
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


def user_directory_path(instance, filename):
    return f'user_{instance.id}/{filename}'


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        if username is None:
            raise TypeError('User must have an username')
        if email is None:
            raise TypeError('User must have an email')
        if password is None:
            raise TypeError('User must have a password')

        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password, **kwargs):
        user = self.create_user(username, email, password, **kwargs)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, unique=True, max_length=255)
    email = models.EmailField(db_index=True, unique=True, blank=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to=user_directory_path)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.email}'
