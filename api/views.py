from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import MarcaSerializer, ProductoSerializer
from .models import Marca, Producto

# Create your views here.

# views de marca
@api_view(['GET'])
def get_marcas(request):
  marcas = Marca.objects.all()
  serializer = MarcaSerializer(marcas, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def create_marcas(request):
  serializer = MarcaSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

# views productos

@api_view(['GET'])
def get_productos(request):
  productos = Producto.objects.all()
  serializer = ProductoSerializer(productos, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def create_producto(request):
  serializer = ProductoSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)
