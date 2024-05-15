
from django.db import models

# Create your models here.

class Categoria(models.Model):
  nom_categoria = models.CharField(max_length=80)

  def __str__(self):
    return self.nom_categoria

class Marca(models.Model):
  nom_marca = models.CharField(max_length=80)

  def __str__(self):
    return self.nom_marca

class Producto(models.Model):
  nombre = models.CharField(max_length=100)
  precio = models.IntegerField()
  descripcion = models.TextField()
  imagen_url = models.URLField(default='')
  stock = models.IntegerField(default=0)
  marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
  categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True)

  def __str__(self):
    return self.nombre