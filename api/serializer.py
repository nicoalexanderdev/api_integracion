from rest_framework import serializers
from .models import Marca, Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nom_categoria')

class MarcaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Marca
    fields = ('id', 'nom_marca')

class ProductoSerializer(serializers.ModelSerializer):
    
    marca = MarcaSerializer()
    categoria = CategoriaSerializer()
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'precio', 'descripcion', 'image_url', 'stock', 'marca', 'categoria')

class ProductoCreateSerializer(serializers.ModelSerializer):
   class Meta:
      model = Producto
      fields = ('id', 'nombre', 'precio', 'descripcion', 'image_url', 'stock', 'marca', 'categoria')
