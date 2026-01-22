from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

from companies.models import Company
from customers.models import Customer
from products.models import Product


class Sale(models.Model):
    """Modelo que representa uma venda."""

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="sales")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="sales")
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT, related_name="sales"
    )
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="sales_created"
    )
    unit_price = models.DecimalField(
        validators=[
            MinValueValidator(0.01, "O preço unitário não pode ser menor que R$ 0.01.")
        ],
        max_digits=10,
        decimal_places=2,
    )
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1, "A quantidade não pode ser menor que 1.")]
    )
    sale_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Configurações do modelo."""

        ordering = ["-sale_date"]
        indexes = [
            models.Index(fields=["company"]),
            models.Index(fields=["sale_date"]),
            models.Index(fields=["product"]),
            models.Index(fields=["customer"]),
        ]

    @property
    def total(self):
        """Calcula o total da venda"""
        if self.unit_price and self.quantity:
            return self.unit_price * self.quantity
        return 0

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return f"Sale #{self.id} - {self.company.name} - R${self.total}"
