from django.contrib import admin

from restapp.models import BillingTransaction


class BillingTransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'amount', 'due_date']


admin.site.register(BillingTransaction, BillingTransactionAdmin)
