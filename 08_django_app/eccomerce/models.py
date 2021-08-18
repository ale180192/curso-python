from django.db import models
from django.db.models.base import Model


class Producto(models.Model):
    nombre = models.CharField(max_length=36)
    stock = models.PositiveSmallIntegerField()
    costo_unitario = models.FloatField()


class Carro(models.Model):
    subtotal = models.FloatField()
    impuestos = models.FloatField()
    total = models.FloatField()
    status = models.CharField(max_length=16)
    items = models.ManyToManyField(to=Producto)

    def actualizar_costos(self):
        print("actualizando costos")
        self.subtotal = 30
        self.total = 50
        self.impuestos = 20


