from django.db import models

# Create your models here.

class Marca(models.Model):
  nom_marca = models.CharField(max_length=80)

  def __str__(self):
    return self.nom_marca

class Producto(models.Model):
  nombre = models.CharField(max_length=100)
  precio = models.IntegerField()
  descripcion = models.TextField()
  marca = models.ForeignKey(Marca, on_delete=models.PROTECT)

def __str__(self):
  return self.nombre