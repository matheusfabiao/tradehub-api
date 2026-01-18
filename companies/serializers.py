from rest_framework import serializers

from companies.models import Company


class CompanySerializer(serializers.ModelSerializer):
    total_revanue = serializers.SerializerMethodField(read_only=True)
    total_sales = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Company
        fields = "__all__"

    def get_total_revanue(self, obj):
        return sum(sale.amount * sale.quantity for sale in obj.sales.all())

    def get_total_sales(self, obj):
        return obj.sales.count()

    def validate_name(self, value):
        if not value.strip()[0].isalpha():
            raise serializers.ValidationError("O primeiro dígito deve ser uma letra.")
        return value
