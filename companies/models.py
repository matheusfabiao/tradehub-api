from django.db import models


class Company(models.Model):
    """Modelo que representa uma empresa."""
    name = models.CharField(max_length=255)
    document = models.CharField(
        max_length=50, unique=True, help_text="CNPJ, EIN ou identificador fiscal"
    )
    industry = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Configurações do modelo."""
        ordering = ["name"]
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.name
