from rest_framework import routers
from django.conf.urls import url, include
from apps.transactions.api.api import TransactionViewSet, TransactionsAggregated


router = routers.DefaultRouter()
router.register(r'transaction', TransactionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^transactions-aggregated', TransactionsAggregated.as_view()),
]
