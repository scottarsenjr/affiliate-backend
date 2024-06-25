from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.core.management import call_command


@shared_task
def parse_affiliate_data():
    print('Parsing started')

    call_command('parse_carriers')

    print('Successfully parsed records')
