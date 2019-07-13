from rest_framework import viewsets, views

from apps.transactions.api.serializers import TransactionSerializer
from apps.transactions.models import Transaction
from rest_framework.response import Response


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionsAggregated(views.APIView):

    def get(self, request, **kwargs):
        transactions = Transaction.objects.all()
        month_hash = {}

        for transaction in transactions:
            month_hash.setDefault(transaction.date.month, 0)
            month_hash[transaction.date.month] += transaction.value

        return Response(month_hash)


