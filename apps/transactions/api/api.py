from rest_framework import viewsets, views

from apps.transactions.api.serializers import TransactionSerializer
from apps.transactions.models import Transaction
from rest_framework.response import Response


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionsAggregated(views.APIView):

    def get(self, request, **kwargs):
        transactions = Transaction.objects.all().order_by('date')
        month_hash = {}

        for transaction in transactions:
            key = transaction.date.strftime("%b-%Y")
            month_hash.setdefault(key, {'spent': 0, 'deposit': 0})
            if transaction.value > 0:
                month_hash[key]['deposit'] += transaction.value
            else:
                month_hash[key]['spent'] -= transaction.value

        return Response(month_hash)


