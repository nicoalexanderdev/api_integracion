from rest_framework import serializers
from .models import Transaccion, Direccion, Region, Provincia, Comuna, Sucursal, Carro, CarroItem, Order, OrderItem, Estado
from django.contrib.auth.models import User
from api.serializer import ProductoSerializer
from user.serializer import UserSerializer 


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
       model = Estado
       fields = ('id', 'nom_estado')

class RegionSerializer(serializers.ModelSerializer):
   class Meta:
      model = Region
      fields = ('id', 'nom_region')

class ProvinciaSerializer(serializers.ModelSerializer):
   
  region = RegionSerializer()

  class Meta:
      model = Provincia
      fields = ('id', 'nom_provincia', 'region')

class ComunaSerializer(serializers.ModelSerializer):
   
  provincia = ProvinciaSerializer()

  class Meta:
      model = Comuna
      fields = ('id', 'nom_comuna', 'provincia')      

class DireccionSerializer(serializers.ModelSerializer):
    
    comuna = ComunaSerializer()

    class Meta:
        model = Direccion
        fields = ('id', 'user', 'direccion', 'num_direccion', 'descripcion', 'comuna')

class DireccionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ('id', 'user', 'direccion', 'num_direccion', 'descripcion', 'comuna')

    def create(self, validated_data):
        return Direccion.objects.create(**validated_data)


class SucursalSerializer(serializers.ModelSerializer):
   
  comuna = ComunaSerializer()

  class Meta:
      model = Sucursal
      fields = ('id', 'nom_sucursal', 'direccion', 'num_direccion', 'comuna')
   

class CarroItemSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()
    subtotal_item = serializers.ReadOnlyField()

    class Meta:
        model = CarroItem
        fields = ['id', 'carro', 'producto', 'cantidad', 'added_at', 'subtotal_item']


class CarroSerializer(serializers.ModelSerializer):
    items = CarroItemSerializer(many=True, read_only=True)
    subtotal_carro = serializers.ReadOnlyField()
    total_items = serializers.ReadOnlyField()

    class Meta:
        model = Carro
        fields = ['id', 'user', 'created_at', 'items', 'subtotal_carro', 'total_items']


class GetTransaccionSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    
    class Meta:
        model = Transaccion
        fields = [
        'id',
        'user', 
        'buy_order', 
        'session_id', 
        'amount', 
        'status', 
        'card_number', 
        'accounting_date', 
        'transaction_date', 
        'authorization_code',
        'payment_type_code',
        'response_code',
        'installments_number'
      ]


class TransaccionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Transaccion
    fields = [
        'id',
        'user', 
        'buy_order', 
        'session_id', 
        'amount', 
        'status', 
        'card_number', 
        'accounting_date', 
        'transaction_date', 
        'authorization_code',
        'payment_type_code',
        'response_code',
        'installments_number'
      ]
    
  def create(self, validated_data):
    return Transaccion.objects.create(**validated_data)
  

class OrderItemSerializer(serializers.ModelSerializer):

    total_item = serializers.ReadOnlyField()

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'producto', 'cantidad', 'total_item']


class GetOrderItemSerializer(serializers.ModelSerializer):
   
   producto = ProductoSerializer()
   total_item = serializers.ReadOnlyField()

   class Meta:
        model = OrderItem
        fields = ['id', 'order', 'producto', 'cantidad', 'total_item']
  

class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'subtotal', 'costo_despacho', 'total', 'transaccion', 'tipo_entrega', 'direccion', 'fecha_entrega', 'estado', 'correo', 'created_at', 'items']

class GetOrdersSerializer(serializers.ModelSerializer):
   
   transaccion = TransaccionSerializer()
   estado = EstadoSerializer()
   items = GetOrderItemSerializer(many=True, read_only=True)

   class Meta:
        model = Order
        fields = ['id', 'user', 'subtotal', 'costo_despacho', 'total', 'transaccion', 'tipo_entrega', 'direccion', 'fecha_entrega', 'estado', 'correo', 'created_at', 'items']

      
   