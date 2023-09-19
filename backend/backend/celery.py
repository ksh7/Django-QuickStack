from __future__ import absolute_import, unicode_literals

import os

from django.conf import settings

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.broker_url = os.environ.get('REDIS_URL', settings.REDIS_CONNECTION_URL)

app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'

app.conf.enable_utc = False

app.conf.timezone = settings.TIME_ZONE

app.conf.beat_schedule = {
    'run-two-times-everyday-contrab': {
        'task': 'fetch_random_coffee_picture',
        'schedule': crontab(hour='9, 17', minute=0,),
    },
}