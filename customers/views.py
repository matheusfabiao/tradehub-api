from rest_framework import generics

from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomerCreateListView(generics.ListCreateAPIView):
    """Lista todos os clientes e cria um novo cliente."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Recupera, atualiza e exclui um cliente."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
