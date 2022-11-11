from django.db import models

from proyectogrupo2_api.Views.ingredients import SKU_INGREDIENT_DICT

# Create your models here.
class OrdenCompra(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    cliente = models.CharField(max_length=300)
    sku = models.IntegerField()
    fechaEntrega = models.BigIntegerField()
    cantidad = models.IntegerField()
    urlNotificacion = models.CharField(max_length=500,blank=True)
    estado = models.CharField(max_length=200)