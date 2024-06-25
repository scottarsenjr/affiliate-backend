from rest_framework import serializers

from .models import CarrierData


class CarrierDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarrierData
        fields = '__all__'
