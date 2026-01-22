from django.contrib import admin

from sales.models import Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "company",
        "product",
        "customer",
        "created_by",
        "unit_price",
        "quantity",
        "sale_date",
        "created_at",
        "updated_at",
    )
    list_filter = ("company", "product", "customer", "created_by")
    search_fields = ("company", "product", "customer", "created_by")
