from rest_framework import serializers
from .models import Marca, Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nom_categoria']

class MarcaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Marca
    fields = ['id', 'nom_marca']

class ProductoSerializer(serializers.ModelSerializer):
    
    marca_nombre = serializers.SerializerMethodField()
    nom_categoria = serializers.SerializerMethodField()
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'descripcion', 'image_url', 'stock', 'marca', 'marca_nombre', 'categoria', 'nom_categoria']

    def get_marca_nombre(self, obj):
        return obj.marca.nom_marca if obj.marca else None

    def get_nom_categoria(self, obj):
        return obj.categoria.nom_categoria if obj.categoria else None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Modificar el queryset para incluir los nombres de las marcas y categorias
        self.fields['marca'].queryset = Marca.objects.all()
        self.fields['categoria'].queryset = Categoria.objects.all()