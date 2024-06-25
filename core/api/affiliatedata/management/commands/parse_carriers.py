from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta
from os import environ as env

import requests
from django.core.management import BaseCommand
from django.utils.timezone import now

from core.api.affiliatedata.models import CarrierData


class Command(BaseCommand):
    help = 'Parse Carriers'

    def handle(self, *args, **options):
        self.stdout.write('Parsing started...')

        self.parse_carriers()

    def parse_carriers(self):
        url = 'https://www.trafficcompany.com/feed/ivr-carrier-performance?access-token={}'.format(
            env['PARSE_ACCESS_TOKEN']
        )

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            with ThreadPoolExecutor(max_workers=4) as executor:
                futures = []
                for item in data:
                    if item.get('carrier_id'):
                        futures.append(executor.submit(self.save_carrier_data, item))
                    else:
                        continue

                for future in futures:
                    future.result()

        except requests.exceptions.RequestException as e:
            self.stdout.write(f'Failed to retrieve data: {str(e)}')

    def save_carrier_data(self, data):
        try:
            carrier_data, created = CarrierData.objects.update_or_create(
                carrier_id=data['carrier_id'],
                defaults={
                    'carrier_name': data['carrier_name'],
                    'country_name': data['country_name'],
                    'ecpc_recent': data['ecpc_recent'],
                    'updated_at': now(),
                },
            )

            carrier_data.update_on_record_time(timedelta(minutes=15))

            if created:
                self.stdout.write(self.style.SUCCESS(f'Created new record for carrier_id {data["carrier_id"]}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Updated record for carrier_id {data["carrier_id"]}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error saving data for carrier_id {data["carrier_id"]}: {str(e)}'))
            raise
