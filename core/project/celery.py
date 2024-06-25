import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.project.settings')

app = Celery('core')
app.loader.override_backends['django-db'] = 'django_celery_results.backends.database:DatabaseBackend'

app.config_from_object('core.project.celeryconfig', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
