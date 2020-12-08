from rest_framework import serializers
from restapp.models.models import BillingTransaction, ExpenseConnectRequestOngoingSupport, ExpenseConnectRequestBulkLesson, \
    BulkLessonRequest, OngoingSupportRequest


class BillingTransactionOutputSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=False)
    # type = serializers.CharField(max_length=256)
    # amount = serializers.CharField(read_only=True)
    # description = serializers.CharField(required=False, default=False)
    # due_date = serializers.DateTimeField(read_only=True)

    def to_representation(self, instance):
        if isinstance(instance, ExpenseConnectRequestBulkLesson):
            return ExpenseConnectRequestBulkLessonSerializer(instance=instance).data
        elif isinstance(instance, ExpenseConnectRequestOngoingSupport):
            return ExpenseConnectRequestOngoingSupportSerializer(instance=instance).data
        else:
            return LaySerializer(instance=instance).data

    # class Meta:
    #     model = BillingTransaction
    #     fields = '__all__'


class LaySerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingTransaction
        fields = '__all__'


class BulkLessonRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkLessonRequest
        fields = '__all__'


class OngoingSupportRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OngoingSupportRequest
        fields = '__all__'


class ExpenseConnectRequestBulkLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseConnectRequestBulkLesson
        fields = '__all__'


class ExpenseConnectRequestOngoingSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseConnectRequestOngoingSupport
        fields = '__all__'
