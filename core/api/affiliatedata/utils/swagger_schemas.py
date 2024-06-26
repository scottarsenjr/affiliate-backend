from drf_yasg import openapi


class CarrierDataViewSetSwaggerSchema:
    @staticmethod
    def get_config():
        from ..serializers import CarrierDataSerializer

        return {
            'responses': {200: CarrierDataSerializer(many=True)},
            'manual_parameters': [
                openapi.Parameter(
                    'order_by',
                    in_=openapi.IN_QUERY,
                    type=openapi.TYPE_STRING,
                    required=False,
                    pattern='^carrier_name|country_name|ecpc_recent|updated_at$',
                ),
                openapi.Parameter(
                    'order_type',
                    in_=openapi.IN_QUERY,
                    type=openapi.TYPE_STRING,
                    required=False,
                    pattern='^asc|desc$',
                ),
            ],
        }
