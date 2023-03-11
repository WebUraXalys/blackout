from django.db import migrations
from django.contrib.auth.models import User


def generate_superuser(apps, schema_editor):
    superuser = User.objects.create_superuser(
                email='',
                username='admin',
                password='admin')

    superuser.save()


class Migration(migrations.Migration):
    dependencies = [
        ('parserapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(generate_superuser),
    ]
