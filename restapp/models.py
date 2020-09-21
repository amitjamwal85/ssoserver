from django.db import models
from model_utils.managers import InheritanceManager

class BulkLessonRequest(models.Model):
    bl_number = models.CharField(max_length=100, null=True)
    bl_request_by = models.CharField(max_length=100, null=True)
    bl_request_to = models.CharField(max_length=100, null=True)


class OngoingSupportRequest(models.Model):
    os_number_bk = models.CharField(max_length=100, null=True)
    os_request_by = models.CharField(max_length=100, null=True)
    os_request_to = models.CharField(max_length=100, null=True)


class BillingTransaction(models.Model):
    type = models.CharField(max_length=100, null=True)
    amount = models.FloatField(default=0)
    description = models.CharField(max_length=500, blank=True, null=True)
    due_date = models.DateTimeField()
    objects = InheritanceManager()


class ExpenseConnectRequestBulkLesson(BillingTransaction):
    bulk_lesson_request = models.ForeignKey(BulkLessonRequest, on_delete=models.DO_NOTHING)


class ExpenseConnectRequestOngoingSupport(BillingTransaction):
    ongoing_support_request = models.ForeignKey(OngoingSupportRequest, on_delete=models.DO_NOTHING)





