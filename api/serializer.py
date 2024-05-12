from rest_framework import serializers
from .models import Marca, Producto

class MarcaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Marca
    fields = ['id', 'nom_marca']

class ProductoSerializer(serializers.ModelSerializer):
    
    marca = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all()) 

    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'imagen_url', 'marca']