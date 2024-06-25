from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'greet_user': {'task': 'core.api.affiliatedata.tasks.parse_affiliate_data', 'schedule': crontab(minute='*/15')}
}
