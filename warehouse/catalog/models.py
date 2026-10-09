from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Назва меблів")
    material = models.CharField(max_length=100, verbose_name="Матеріал")
    dimensions = models.CharField(max_length=100, verbose_name="Розміри")
    color = models.CharField(max_length=50, verbose_name="Колір")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Ціна")

    def __str__(self):
        return f"{self.name} ({self.material}, {self.color})"