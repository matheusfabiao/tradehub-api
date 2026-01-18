from django.db import models

from companies.models import Company


class Customer(models.Model):
    """Modelo que representa um cliente."""
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    document = models.CharField(
        max_length=50, unique=True, help_text="CPF, CNPJ, EIN ou identificador fiscal"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Configurações do modelo."""
        ordering = ["name"]
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        indexes = [
            models.Index(fields=["company"]),
            models.Index(fields=["email"]),
        ]

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.name
