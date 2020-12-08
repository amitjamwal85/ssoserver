from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from restapp.models.models import BillingTransaction
from restapp.serializer.test_inheritance_serializer import BillingTransactionOutputSerializer


from rest_framework.response import Response


def http_response(error, response, status_code):
    final_response = dict()
    final_response['error'] = error
    if error:
        final_response['data'] = [response]
    else:
        final_response['data'] = response
    return Response(final_response, status_code)


class BillingTransactionListRestApi(GenericAPIView):
    permission_classes = (AllowAny, )
    serializer_class = BillingTransactionOutputSerializer
    # queryset = BillingTransaction.objects.all()
    # lookup_field = 'pk'

    def get_queryset(self):
        return BillingTransaction.objects.select_subclasses()

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return http_response(False, serializer.data, status.HTTP_200_OK)



