from rest_framework import serializers

from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    total_spent = serializers.SerializerMethodField(read_only=True)
    total_purchases = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Customer
        fields = "__all__"

    def get_total_spent(self, obj):
        return sum(sale.amount * sale.quantity for sale in obj.sales.all())

    def get_total_purchases(self, obj):
        return obj.sales.count()

    def validate_name(self, value):
        if not value.strip()[0].isalpha():
            raise serializers.ValidationError("O primeiro dígito deve ser uma letra.")
        return value
