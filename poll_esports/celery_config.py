import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'poll_esports.settings')

app = Celery('poll_esports')

app.conf.broker_connection_retry_on_startup = True

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule_filename = '/tmp/celerybeat-schedule'
app.autodiscover_tasks()
