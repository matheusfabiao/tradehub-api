from rest_framework import serializers

from sales.models import Sale


class SaleSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Sale."""

    total = serializers.SerializerMethodField(read_only=True)
    unit_price = serializers.SerializerMethodField(read_only=True)

    class Meta:
        """Configurações do serializer."""

        model = Sale
        fields = "__all__"

    def get_total(self, obj):
        """Calcula o total da venda."""
        return obj.amount * obj.quantity

    def get_unit_price(self, obj):
        """Calcula o preço unitário."""
        if obj.quantity == 0:
            return 0
        return obj.amount

    def validate_sale_date(self, value):
        """Valida a data da venda."""
        if value < self.instance.created_at.date():
            raise serializers.ValidationError(
                "A data da venda não pode ser menor que a data de criação."
            )
        return value
