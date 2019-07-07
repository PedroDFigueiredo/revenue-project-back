from rest_framework import viewsets

from apps.transactions.api.serializers import TransactionSerializer
from apps.transactions.models import Transaction


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
