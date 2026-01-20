from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app.permissions import GlobalDefaultPermission
from companies.models import Company
from companies.serializers import CompanySerializer


class CompanyCreateListView(generics.ListCreateAPIView):
    """Lista todas as empresas e cria uma nova empresa."""

    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Recupera, atualiza e exclui uma empresa."""

    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
