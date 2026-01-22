from django.db.models import F, Sum
from rest_framework import generics, response, status, views
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


class SaleStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Sale.objects.all()

    def get(self, request):
        total_sales = self.queryset.count()
        total_revanue = self.queryset.aggregate(
            total_revanue=Sum(F("unit_price") * F("quantity"))
        )

        return response.Response(
            data={
                "total_sales": total_sales,
                "total_revanue": total_revanue["total_revanue"],
            },
            status=status.HTTP_200_OK,
        )
