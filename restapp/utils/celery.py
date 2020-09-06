import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ssoserver.settings')
app = Celery('ssoserver')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'add-every-5-seconds': {
        # 'task': 'restapp.utils.celery_task.loop_counter',
        'task': 'cron_task',
        'schedule': 5.0,
        'args': ('hari', )
    }
    # 'add-every-minute-contrab': {
    #     'task': 'data_checking',
    #     'schedule': crontab(minute=1),
    # },
}

app.autodiscover_tasks()


