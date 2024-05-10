from rest_framework import serializers
from .models import Marca, Producto

class MarcaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Marca
    fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    
    marca = serializers.StringRelatedField(many=False) 

    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'marca']