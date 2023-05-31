import django_filters
from .models import Buildings


class BuildingFilter(django_filters.FilterSet):
    street = django_filters.CharFilter(field_name='Street__Name')
    city = django_filters.CharFilter(field_name='Street__City')

    class Meta:
        model = Buildings
        fields = ['street', 'city']
