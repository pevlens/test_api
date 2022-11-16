import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_transaction.settings')

app = Celery('site_transaction')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

from transaction.tasks import send_spam
app.conf.beat_schedule = {
    'send-email-every-1-minute':{
        'task': 'site_transaction.celery.send_spam_bute',
        'schedule': crontab(hour="7")
    }
}



@app.task
def send_spam_bute():
    send_spam()

    
