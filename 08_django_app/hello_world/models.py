from django.db import models


class Producto(models.Model):
    name = models.CharField(max_length=30)
    stock = models.PositiveSmallIntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)