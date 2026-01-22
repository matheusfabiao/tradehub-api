from rest_framework import serializers

from sales.models import Sale


class SaleSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Sale."""

    total = serializers.SerializerMethodField(read_only=True)

    class Meta:
        """Configurações do serializer."""

        model = Sale
        fields = "__all__"

    def get_total(self, obj):
        """Calcula o total da venda."""
        return obj.unit_price * obj.quantity

    def validate_sale_date(self, value):
        """Valida a data da venda."""
        if value < self.instance.created_at.date():
            raise serializers.ValidationError(
                "A data da venda não pode ser menor que a data de criação."
            )
        return value
