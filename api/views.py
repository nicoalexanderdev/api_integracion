from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import MarcaSerializer, CategoriaSerializer, ProductoSerializer, ProductoCreateSerializer
from .models import Marca, Categoria, Producto
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

# views de marca

# obtener todas las marcas
@api_view(['GET'])
def get_marcas(request):
  marcas = Marca.objects.all()
  serializer = MarcaSerializer(marcas, many=True)
  return Response(serializer.data)


# agregar marca
@api_view(['POST'])
def create_marcas(request):
  serializer = MarcaSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)


# obtener solo una marca
@api_view(['GET'])
def get_marca(request, pk):
  marca = Marca.objects.get(id=pk)
  serializer = MarcaSerializer(marca, many=False)
  return Response(serializer.data)

# actualizar marca
@api_view(['PUT'])
def update_marca(request, pk):
  marca = Marca.objects.get(id=pk)
  serializer = MarcaSerializer(instance=marca, data=request.data)

  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

# eliminar marca
@api_view(['DELETE'])
def delete_marca(request, pk):
  marca = Marca.objects.get(id=pk)
  marca.delete()

  return Response('Marca eliminada')





# views productos

# obtener todos los productos
@api_view(['GET'])
def get_productos(request):
  productos = Producto.objects.all()
  serializer = ProductoSerializer(productos, many=True)
  return Response(serializer.data)

# agregar producto
@api_view(['POST'])
def create_producto(request):
  parser_classes = (MultiPartParser, FormParser)
  serializer = ProductoCreateSerializer(data=request.data, context={'request': request})
  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

# obtener solo un producto
@api_view(['GET'])
def get_producto(request, pk):
  producto = Producto.objects.get(id=pk)
  serializer = ProductoSerializer(producto, many=False)
  return Response(serializer.data)

# actualizar producto
@api_view(['PUT'])
def update_producto(request, pk):
  producto = Producto.objects.get(id=pk)
  serializer = ProductoSerializer(instance=producto, data=request.data)

  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

# eliminar producto
@api_view(['DELETE'])
def delete_producto(request, pk):
  producto = Producto.objects.get(id=pk)
  producto.delete()

  return Response('Producto eliminado')

# filtrar producto por categorias
@api_view(['GET'])
def get_productos_categoria(request, pk):
    try:
        categoria = get_object_or_404(Categoria, id=pk)
        productos = Producto.objects.filter(categoria=categoria)
        if not productos:
            return Response({'detail': 'No hay productos de esta categoria'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductoSerializer(productos, many=True)

        response_data = {
          'categoria': categoria.nom_categoria,
          'productos': serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Producto.DoesNotExist:
        return Response({'detail': 'Categoria no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# filtrar producto por marca
@api_view(['GET'])
def get_productos_marca(request, pk):
    try:
        marca = get_object_or_404(Marca, id=pk)
        productos = Producto.objects.filter(marca=marca)
        if not productos:
            return Response({'detail': 'No hay productos de esta marca'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductoSerializer(productos, many=True)

        response_data = {
          'marca': marca.nom_marca,
          'productos': serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Producto.DoesNotExist:
        return Response({'detail': 'Marca no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  # views de categorias

# obtener todas las categorias
@api_view(['GET'])
def get_categorias(request):
  categorias = Categoria.objects.all()
  serializer = CategoriaSerializer(categorias, many=True)
  return Response(serializer.data)


# agregar categoria
@api_view(['POST'])
def create_categoria(request):
  serializer = CategoriaSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

# actualizar categoria
@api_view(['PUT'])
def update_categoria(request, pk):
  categoria = Categoria.objects.get(id=pk)
  serializer = CategoriaSerializer(instance=categoria, data=request.data)

  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

# obtener solo una categoria
@api_view(['GET'])
def get_categoria(request, pk):
  categoria = Categoria.objects.get(id=pk)
  serializer = CategoriaSerializer(categoria, many=False)
  return Response(serializer.data)

# eliminar categoria
@api_view(['DELETE'])
def delete_categoria(request, pk):
  categoria = Categoria.objects.get(id=pk)
  categoria.delete()

  return Response('Categoria eliminada')