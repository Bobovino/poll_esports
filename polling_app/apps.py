from django.apps import AppConfig
from django.conf import settings
from polling_app.tasks import poll_esports_task


class PollingAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polling_app'
    
