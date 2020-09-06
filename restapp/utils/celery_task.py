from celery import shared_task
from time import sleep

from celery.task import periodic_task


@shared_task
def loop_counter(loop_count):
    for i in range(loop_count):
        print(f"value of i: {i}")
        sleep(1)
    return "Done"


@shared_task(name='cron_task')
def cron_task(task_name):
    print(f"task_name : {task_name}")
    return task_name
