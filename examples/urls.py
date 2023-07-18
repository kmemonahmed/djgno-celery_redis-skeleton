from .celery_beat_test.views import test_celery_beat_view
from django.urls import path

urlpatterns = [
    path('test-celery-beat/', test_celery_beat_view, name='test_celery_beat'),
]
