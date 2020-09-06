from django.http import HttpResponse
from restapp.utils.celery_task import loop_counter


def celery_task(request):
    loop_counter.delay(10)
    return HttpResponse("ok")
