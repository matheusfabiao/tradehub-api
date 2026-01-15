from django.contrib import admin

from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "company")
    list_filter = ("company",)
    search_fields = ("name", "email")
