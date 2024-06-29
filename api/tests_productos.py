import tempfile
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from .views import get_productos, create_producto, get_producto
from .models import Producto, Marca, Categoria  
from .serializer import ProductoSerializer, ProductoCreateSerializer
from django.core.files.uploadedfile import SimpleUploadedFile 
from PIL import Image

class ProductoAPITests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.marca = Marca.objects.create(nom_marca='Marca Test')
        self.categoria = Categoria.objects.create(nom_categoria='Categoría Test')

        self.producto1 = Producto.objects.create(
            nombre='Producto 1',
            precio=100,
            descripcion='Descripción del Producto 1',
            stock=10,
            marca=self.marca,
            categoria=self.categoria
        )
        self.producto2 = Producto.objects.create(
            nombre='Producto 2',
            precio=200,
            descripcion='Descripción del Producto 2',
            stock=20,
            marca=self.marca,
            categoria=self.categoria
        )

    def test_get_productos(self):

        request = self.factory.get('')
        response = get_productos(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer = ProductoSerializer(instance=[self.producto1, self.producto2], many=True)
        self.assertEqual(response.data, serializer.data)



class ProductoCreateAPITests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.marca = Marca.objects.create(nom_marca='Marca Test')
        self.categoria = Categoria.objects.create(nom_categoria='Categoría Test')

    def test_create_producto(self):

        # Crea una imagen temporal para la prueba
        image = Image.new('RGB', (100, 100))
        temp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(temp_file, format='JPEG')
        temp_file.seek(0)

        producto_data = {
            'nombre': 'Producto Test',
            'precio': 100,
            'descripcion': 'Descripción del Producto Test',
            'stock': 10,
            'marca': self.marca.id,
            'categoria': self.categoria.id,
            'image_url': SimpleUploadedFile(temp_file.name, temp_file.read(), content_type='image/jpeg')
        }

        request = self.factory.post('/create-producto/', producto_data, format='multipart')
        response = create_producto(request)

        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_201_CREATED])

        if not Producto.objects.filter(nombre='Producto Test').exists():
            print("Errores del serializador:", response.data)

        self.assertTrue(Producto.objects.filter(nombre='Producto Test').exists())

        producto_creado = Producto.objects.get(nombre='Producto Test')
        serializer = ProductoCreateSerializer(instance=producto_creado)
        
        response_data = response.data
        serializer_data = serializer.data
        response_data['image_url'] = response_data['image_url'].replace('http://testserver', '')
        
        self.assertEqual(response_data, serializer_data)

        self.assertTrue(producto_creado.image_url.name.startswith('images/'))



class ProductoGetAPITests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.marca = Marca.objects.create(nom_marca='Marca Test')
        self.categoria = Categoria.objects.create(nom_categoria='Categoría Test')

        self.producto = Producto.objects.create(
            nombre='Producto Test',
            precio=100,
            descripcion='Descripción del Producto Test',
            stock=10,
            marca=self.marca,
            categoria=self.categoria
        )

    def test_get_producto(self):

        request = self.factory.get(f'/get-producto/{self.producto.id}/')
        response = get_producto(request, pk=self.producto.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer = ProductoSerializer(instance=self.producto)
        self.assertEqual(response.data, serializer.data)


