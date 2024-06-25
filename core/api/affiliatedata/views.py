from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import \
    OrderingFilter  # Import OrderingFilter for ordering

from .filters import CarrierDataFilter
from .models import CarrierData
from .serializers import CarrierDataSerializer


class CarrierDataViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = CarrierData.objects.all()
    serializer_class = CarrierDataSerializer

    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )

    filterset_class = CarrierDataFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        order_by = self.request.query_params.get('order_by')
        order_type = self.request.query_params.get('order_type', 'asc')

        if order_by:
            if order_type == 'asc':
                queryset = queryset.order_by(order_by)
            elif order_type == 'desc':
                queryset = queryset.order_by(f'-{order_by}')

        return queryset
