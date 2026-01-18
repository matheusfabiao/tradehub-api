from django.core.validators import MinValueValidator
from django.db import models

from companies.models import Company


class Product(models.Model):
    """Modelo que representa um produto."""

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sku = models.CharField(
        max_length=50, unique=True, help_text="Código interno do produto"
    )
    price = models.DecimalField(
        validators=[
            MinValueValidator(0.00, "O preço não pode ser menor que 0.00."),
        ],
        max_digits=10,
        decimal_places=2,
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Configurações do modelo."""

        ordering = ["name"]
        unique_together = ("company", "sku")
        verbose_name = "Product"
        verbose_name_plural = "Products"
        indexes = [
            models.Index(fields=["company"]),
            models.Index(fields=["sku"]),
        ]

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return f"{self.name} ({self.company.name})"
