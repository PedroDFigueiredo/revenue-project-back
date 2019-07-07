from rest_framework import routers
from django.conf.urls import url, include
from apps.transactions.api.api import TransactionViewSet

router = routers.DefaultRouter()
router.register(r'transaction', TransactionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
