from django.db import models
from django.contrib.auth.models import User

# Create your models here.request

class Region(models.Model):
    nom_region = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom_region


class Provincia(models.Model):
    nom_provincia = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='provincias')

    class Meta:
        unique_together = ('nom_provincia', 'region')

    def __str__(self):
        return self.nom_provincia


class Comuna(models.Model):
    nom_comuna = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name='comunas')

    class Meta:
        unique_together = ('nom_comuna', 'provincia')

    def __str__(self):
        return self.nom_comuna

class Direccion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='direcciones')
    direccion = models.CharField(max_length=100)
    num_direccion = models.IntegerField()
    descripcion = models.IntegerField(null=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name='direcciones')

    def __str__(self):
        return f'{self.direccion} {self.num_direccion}, {self.comuna.nom_comuna}, {self.comuna.provincia.nom_provincia}, {self.comuna.provincia.region.nom_region}'

class Sucursal(models.Model):
    nom_sucursal = models.CharField(max_length=80)
    direccion = models.CharField(max_length=100)
    num_direccion = models.IntegerField()
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name='sucursales')

    def __str__(self):
        return self.nom_sucursal

class Transaccion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buy_order = models.CharField(max_length=50)
    session_id = models.CharField(max_length=50)
    amount = models.IntegerField()
    status = models.CharField(max_length=20)
    card_number = models.CharField(max_length=4)
    accounting_date = models.CharField(max_length=10)
    transaction_date = models.CharField(max_length=50)
    authorization_code = models.CharField(max_length=10)
    payment_type_code = models.CharField(max_length=10)
    response_code = models.IntegerField()
    installments_number = models.IntegerField()

    def __str__(self):
        return f'Transaccion {self.buy_order} - {self.status}'