from django.conf import settings

from core.project.periodic_tasks import CELERY_BEAT_SCHEDULE  # noqa:F401

# CELERY SETTINGS
broker_url = (
    settings.CACHES['celery_broker']['LOCATION'] if 'celery_broker' in settings.CACHES else 'redis://localhost:6379/1'
)

cache_backend = (
    settings.CACHES['celery_cache_backend']['LOCATION']
    if 'celery_cache_backend' in settings.CACHES
    else 'redis://localhost:6379/2'
)

accept_content = ['json']
task_serializer = 'json'
timezone = 'Europe/Moscow'
result_backend = 'django-db'
