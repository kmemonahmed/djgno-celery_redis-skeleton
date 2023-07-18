from __future__ import absolute_import, unicode_literals
from django.conf import settings
import os

from celery import Celery
from celery.schedules import crontab
from examples.celery_beat_test.tasks import test_celery_beat

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_skeleton.settings')

app = Celery('celery_skeleton')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Dhaka')

app.config_from_object(settings, namespace='CELERY')

# celery beat settings
app.conf.beat_schedule = {
    # example task to be executed every 30 seconds
    'add-every-30-seconds': {
        'task': 'examples.celery_beat_test.tasks.test_celery_beat',
        'schedule': crontab(hour=12, minute=51),
    },
}


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')