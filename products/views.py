from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from products.serializers import ProductSerializer


class ProductCreateListView(generics.ListCreateAPIView):
    """Lista todos os produtos e cria um novo produto."""

    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Recupera, atualiza e exclui um produto."""

    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
