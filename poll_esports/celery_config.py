os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

app = Celery('your_project')

class CeleryAppConfig(AppConfig):
import os
from celery import Celery
from django.apps import apps, AppConfig
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

app = Celery('your_project')

class CeleryAppConfig(AppConfig):
    name = 'your_project.celery_app'
    verbose_name = 'Celery Config'

    def ready(self):
        if not settings.configured:
            # Set the default Django settings module for the 'celery' program.
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
        app.config_from_object('django.conf:settings', namespace='CELERY')
        app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])

app_config = CeleryAppConfig()
app_config.ready()
