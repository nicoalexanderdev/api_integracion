from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import MarcaSerializer, ProductoSerializer
from .models import Marca, Producto

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
  serializer = ProductoSerializer(data=request.data, context={'request': request})
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