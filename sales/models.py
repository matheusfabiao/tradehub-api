from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

from companies.models import Company
from customers.models import Customer
from products.models import Product


class Sale(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="sales")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="sales")
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT, related_name="sales"
    )
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="sales_created"
    )
    amount = models.DecimalField(
        validators=[
            MinValueValidator(1.00, "O valor da venda não pode ser menor que R$ 1.00.")
        ],
        max_digits=10,
        decimal_places=2,
        help_text="Valor total da venda",
    )
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1), "A quantidade não pode ser menor que 1."]
    )
    sale_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["company"]),
            models.Index(fields=["sale_date"]),
            models.Index(fields=["product"]),
            models.Index(fields=["customer"]),
        ]
        ordering = ["-sale_date"]

    def __str__(self):
        return f"Sale #{self.id} - {self.company.name}"
