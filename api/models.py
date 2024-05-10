from django.db import models

# Create your models here.

class Marca(models.Model):
  nom_marca = models.Charfield(max_length=80)

  def __str__(self):
    return self.nom_marca

class Producto(models.Model):
  nombre = models.Charfield(max_length=100)
  precio = models.Integerfield()
  descripcion = models.Textfield()
  marca = models.ForeignKey(Marca, on_delete=models.PROTECTED)

def __str__(self):
  return self.nombre


