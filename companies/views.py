from rest_framework import generics

from companies.models import Company
from companies.serializers import CompanySerializer


class CompanyCreateListView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
