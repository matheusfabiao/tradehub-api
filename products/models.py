from django.db import models

from companies.models import Company


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sku = models.CharField(
        max_length=50, unique=True, help_text="Código interno do produto"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        unique_together = ("company", "sku")
        verbose_name = "Product"
        verbose_name_plural = "Products"
        indexes = [
            models.Index(fields=["company"]),
            models.Index(fields=["sku"]),
        ]

    def __str__(self):
        return f"{self.name} ({self.company.name})"
