import django_filters

from .models import CarrierData


class CarrierDataFilter(django_filters.FilterSet):
    min_ecpc = django_filters.NumberFilter(field_name='ecpc_recent', lookup_expr='gte')
    carrier_name = django_filters.CharFilter(field_name='carrier_name', lookup_expr='icontains')
    country_name = django_filters.CharFilter(field_name='country_name', lookup_expr='icontains')

    class Meta:
        model = CarrierData
        fields = ['min_ecpc', 'carrier_name', 'country_name']
