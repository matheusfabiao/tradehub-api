from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    document = models.CharField(
        max_length=50, unique=True, help_text="CNPJ, EIN ou identificador fiscal"
    )
    industry = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name
