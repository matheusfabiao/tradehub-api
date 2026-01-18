from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Product."""

    total_revenue = serializers.SerializerMethodField(read_only=True)
    total_sold = serializers.SerializerMethodField(read_only=True)

    class Meta:
        """Configurações do serializer."""

        model = Product
        fields = "__all__"

    def get_total_revenue(self, obj):
        """Calcula o total de receita."""
        return sum(sale.amount * sale.quantity for sale in obj.sales.all())

    def get_total_sold(self, obj):
        """Calcula o total de vendas."""
        return sum(sale.quantity for sale in obj.sales.all())

    def validate_name(self, value):
        """Valida o nome do produto."""
        if not value.strip()[0].isalpha():
            raise serializers.ValidationError("O primeiro dígito deve ser uma letra.")
        return value
