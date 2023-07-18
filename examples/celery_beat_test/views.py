from django.http import HttpResponse
from .tasks import test_celery_beat
from django.utils import timezone
import json

# imports for celery beat
from celery import shared_task
from celery.schedules import crontab
from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule


# Create your views here.
def test_celery_beat_view(request):
    time = timezone.localtime()
    minute = time.minute
    hour = time.hour
    day_of_week = time.strftime('%a')
    day = time.day
    month = time.month

    schedule, created = CrontabSchedule.objects.get_or_create(
        hour=hour,
        minute=minute + 1,
        day_of_week=day_of_week,
        day_of_month=day,
        month_of_year=month,
    )
   
    if PeriodicTask.objects.filter(name='test_celery_beat_s').exists():
        PeriodicTask.objects.filter(name='test_celery_beat_s').delete()
    task = PeriodicTask.objects.create(
        crontab=schedule, name='test_celery_beat_s', 
        task='examples.celery_beat_test.tasks.test_celery_beat', 
        args=json.dumps([1, 2]), kwargs=json.dumps({'test': 'test'}),
        one_off=True,
    )
    return HttpResponse(f'You haved successfully done setup for Celery Beat! Check your celry terminal for output in {hour}:{minute + 1} {day_of_week} {day}/{month}.')