from django.http import HttpResponse
from .tasks import test_celery_beat

# imports for celery beat
from celery import shared_task
from celery.schedules import crontab


# Create your views here.
def test_celery_beat(request):
    return HttpResponse('You haved successfully done setup for Celery Beat! Check your terminal for output after 30 seconds.')