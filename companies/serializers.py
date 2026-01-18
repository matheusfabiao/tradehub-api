from rest_framework import serializers

from companies.models import Company


class CompanySerializer(serializers.ModelSerializer):
    """Serializer para o modelo Company."""
    total_revanue = serializers.SerializerMethodField(read_only=True)
    total_sales = serializers.SerializerMethodField(read_only=True)

    class Meta:
        """Configurações do serializer."""
        model = Company
        fields = "__all__"

    def get_total_revanue(self, obj):
        """Calcula o total de receita."""
        return sum(sale.amount * sale.quantity for sale in obj.sales.all())

    def get_total_sales(self, obj):
        """Calcula o total de vendas."""
        return obj.sales.count()

    def validate_name(self, value):
        """Valida o nome da empresa."""
        if not value.strip()[0].isalpha():
            raise serializers.ValidationError("O primeiro dígito deve ser uma letra.")
        return value
