from rest_framework import serializers

from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Customer."""
    total_spent = serializers.SerializerMethodField(read_only=True)
    total_purchases = serializers.SerializerMethodField(read_only=True)

    class Meta:
        """Configurações do serializer."""
        model = Customer
        fields = "__all__"

    def get_total_spent(self, obj):
        """Calcula o total gasto pelo cliente."""
        return sum(sale.amount * sale.quantity for sale in obj.sales.all())

    def get_total_purchases(self, obj):
        """Calcula o total de compras do cliente."""
        return obj.sales.count()

    def validate_name(self, value):
        """Valida o nome do cliente."""
        if not value.strip()[0].isalpha():
            raise serializers.ValidationError("O primeiro dígito deve ser uma letra.")
        return value
