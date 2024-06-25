from datetime import timedelta

from django.db import models


class CarrierData(models.Model):
    carrier_id = models.IntegerField(primary_key=True)
    carrier_name = models.CharField(max_length=100)
    country_name = models.CharField(max_length=100)
    ecpc_recent = models.FloatField()
    updated_at = models.DateTimeField(auto_now_add=True)
    on_record = models.BigIntegerField(default=0)

    def __str__(self):
        return self.carrier_name

    def update_on_record_time(self, additional_time: timedelta):
        self.on_record += additional_time.total_seconds()
        self.save()
