from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app.permissions import GlobalDefaultPermission
from sales.models import Sale
from sales.serializers import SaleSerializer


class SaleCreateListView(generics.ListCreateAPIView):
    """Lista todas as vendas e cria uma nova venda."""

    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SaleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Recupera, atualiza e exclui uma venda."""

    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
