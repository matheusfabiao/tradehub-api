from rest_framework import generics

from products.models import Product
from products.serializers import ProductSerializer


class ProductCreateListView(generics.ListCreateAPIView):
    """Lista todos os produtos e cria um novo produto."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Recupera, atualiza e exclui um produto."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
