from rest_framework import generics

from sales.models import Sale
from sales.serializers import SaleSerializer


class SaleCreateListView(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SaleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
