from rest_framework import serializers
from .models import Transaccion, Direccion, Region, Provincia, Comuna

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


class TransaccionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Transaccion
    fields = [
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