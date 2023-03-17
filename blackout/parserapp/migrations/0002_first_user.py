import string
from random import choice
from django.db import migrations
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail


def create_temporary_key(length):
    # Define the set of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password of the specified length
    password = ''.join(choice(characters) for i in range(length))

    return password


def generate_superuser(apps, schema_editor):
    username = create_temporary_key(15)
    password = create_temporary_key(15)


    superuser = User.objects.create_superuser(
                email=settings.EMAIL_HOST_USER,
                username=username,
                password=password)

    superuser.save()

    send_mail('Default password and username', f'Username {username} Password {password}',
                settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])



class Migration(migrations.Migration):
    dependencies = [
        ('parserapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(generate_superuser),
    ]
