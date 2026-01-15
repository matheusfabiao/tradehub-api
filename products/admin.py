from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "sku", "price", "is_active")
    list_filter = ("company", "is_active")
    search_fields = ("name", "sku")
