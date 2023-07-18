from celery import shared_task

@shared_task(bind=True)
def test_celery_beat(self, *args, **kwargs):
    args = list(args)
    kwargs = dict(kwargs)
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    
    for i in range(10):
        print(i)
    return 'done from celery beat'