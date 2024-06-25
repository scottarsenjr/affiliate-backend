from datetime import timedelta

from core.project.periodic_tasks import CELERY_BEAT_SCHEDULE

# CELERY SETTINGS
broker_url = 'redis://localhost:6379/1'
cache_backend = 'redis://localhost:6379/2'
accept_content = ['json']
task_serializer = 'json'
timezone = 'Europe/Moscow'
result_backend = 'django-db'
