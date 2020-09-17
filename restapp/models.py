from django.db import models


class BillingTransaction(models.Model):
    type = models.CharField(max_length=100, null=True)
    amount = models.FloatField(default=0)
    due_date = models.DateTimeField()
