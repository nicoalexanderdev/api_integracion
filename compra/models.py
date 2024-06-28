from django.db import models
from django.contrib.auth.models import User

from api.models import Producto

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
    

class Carro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carro de {self.user.username}"

    def subtotal_carro(self):
        return sum(item.subtotal_item() for item in self.items.all())

    def total_items(self):
        return sum(item.cantidad for item in self.items.all())
    

class CarroItem(models.Model):
    carro = models.ForeignKey(Carro, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombre}"

    def subtotal_item(self):
        return self.producto.precio * self.cantidad
    
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subtotal = models.PositiveBigIntegerField()
    costo_despacho = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    tipo_entrega = models.CharField(max_length=10)
    direccion = models.TextField()
    fecha_entrega = models.DateField()
    correo = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orden #{self.id} de {self.user.username}"
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombre} de la orden #{self.order.id}"

    def total_item(self):
        return self.producto.precio * self.cantidad


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