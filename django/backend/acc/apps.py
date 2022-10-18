from django.apps import AppConfig
from django.core.signals import request_finished
 
 
class AccConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'acc'
 
    def ready(self):
        import acc.signals