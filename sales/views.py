from rest_framework import generics

from sales.models import Sale
from sales.serializers import SaleSerializer


class SaleCreateListView(generics.ListCreateAPIView):
    """Lista todas as vendas e cria uma nova venda."""
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SaleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Recupera, atualiza e exclui uma venda."""
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
