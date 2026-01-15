from django.contrib import admin

from companies.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "industry")
    list_filter = ("industry",)
    search_fields = ("name",)
