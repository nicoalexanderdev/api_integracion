from rest_framework import serializers
from .models import Marca, Producto

class MarcaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Marca
    fields = ['id', 'nom_marca']

class ProductoSerializer(serializers.ModelSerializer):
    
    marca_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'descripcion', 'imagen_url', 'marca', 'marca_nombre']

    def get_marca_nombre(self, obj):
        return obj.marca.nom_marca if obj.marca else None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Modificar el queryset para incluir los nombres de las marcas
        self.fields['marca'].queryset = Marca.objects.all()