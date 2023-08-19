from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'icon', 'is_staff', 'is_superuser', 'is_active', 'updated', 'created', 'last_login']

