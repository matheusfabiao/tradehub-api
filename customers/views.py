from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app.permissions import GlobalDefaultPermission
from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomerCreateListView(generics.ListCreateAPIView):
    """Lista todos os clientes e cria um novo cliente."""

    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Recupera, atualiza e exclui um cliente."""

    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
