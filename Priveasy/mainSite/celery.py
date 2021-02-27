from django.conf import settings
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'Priveasy.settings.pro')

app = Celery('mainSite')
app.config_from_object('django.conf:settings' , namespace = 'CELERY')
app.autodiscover_tasks()
