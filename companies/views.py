from rest_framework import generics

from companies.models import Company
from companies.serializers import CompanySerializer


class CompanyCreateListView(generics.ListCreateAPIView):
    """Lista todas as empresas e cria uma nova empresa."""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Recupera, atualiza e exclui uma empresa."""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
