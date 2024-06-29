
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from .views import region, provincia, comuna, sucursal, direccion, agregar_direccion, crear_orden_compra, order_items, transbank_create
from .models import Region, Provincia, Comuna, Direccion, Sucursal, Transaccion, Estado, Order, OrderItem
from .serializer import RegionSerializer, ProvinciaSerializer, ComunaSerializer, DireccionSerializer, DireccionCreateSerializer, SucursalSerializer, TransaccionSerializer, OrderItemSerializer, OrderSerializer 
from django.urls import reverse
from django.contrib.auth.models import User
from api.models import Producto, Marca, Categoria
from api.serializer import ProductoSerializer, ProductoCreateSerializer
import json

# Create your tests here.
'''
class RegionGetAPITests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_get_region(self):

        Region.objects.create(nom_region='Region 1')
        Region.objects.create(nom_region='Region 2')

        request = self.factory.get('/region/')
        response = region(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 2)  
'''


'''
class ProvinciaGetAPITests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_get_provincias_por_region(self):
        region = Region.objects.create(nom_region='Región Test')
        provincia1 = Provincia.objects.create(nom_provincia='Provincia 1', region=region)
        provincia2 = Provincia.objects.create(nom_provincia='Provincia 2', region=region)

        request = self.factory.get(f'/provincia/{region.id}')
        response = provincia(request, id=region.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        # Verificar que los datos de las provincias coinciden
        serializer = ProvinciaSerializer([provincia1, provincia2], many=True)
        self.assertEqual(response.data, serializer.data)

    def test_provincia_invalid_id(self):

        request = self.factory.get(f'/provincia/{999}')
        response = provincia(request, id=999)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
'''


'''
class OrdenCompraCreate(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.user = User.objects.create_user(username='testuser', password='password')

        self.estado = Estado.objects.create(nom_estado='estado 1')
        self.transaccion = Transaccion.objects.create(
            user_id=self.user.id,
            buy_order='BO-123',
            session_id='19',
            amount=50000,
            status='Aprobado',
            card_number='7798',
            accounting_date='acountdate',
            transaction_date='29-06-2024',
            authorization_code='1928',
            payment_type_code='4647',
            response_code=1819,
            installments_number=123
        )

    def test_create_order(self):

        order_data = {
            'user': self.user.id,
            'subtotal': 1234,
            'costo_despacho': 3990,
            'total': 123445,
            'tipo_entrega': 'despacho',
            'direccion': 'direccion 1',
            'fecha_entrega': '2024-07-04',
            'correo': 'asd@correo.com',
            'transaccion': self.transaccion.id,
            'estado': self.estado.id
        }

        request = self.factory.post('/crear-orden-compra/', order_data)
        response = crear_orden_compra(request)

        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_201_CREATED])

        orden_creada = Order.objects.get(id=1)
        serializer = OrderSerializer(instance=orden_creada)

        response_data = response.data
        serializer_data = serializer.data

        self.assertEqual(response_data, serializer_data)
'''


'''
class AgregarDireccionTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.user = User.objects.create_user(username='testuser', password='password')
        self.region = Region.objects.create(nom_region='region 1')
        self.provincia = Provincia.objects.create(nom_provincia='provincia 1', region=self.region)
        self.comuna = Comuna.objects.create(nom_comuna='comuna 1', provincia=self.provincia)

    def test_agregar_direccion(self):

        direccion_data = {
            'user': self.user.id,
            'direccion': 'direccion',
            'num_direccion': 23,
            'descripcion': '',
            'comuna': self.comuna.id
        }

        request = self.factory.post('/agregar-direccion/', direccion_data)
        response = agregar_direccion(request)

        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_201_CREATED])

        direccion_creada = Direccion.objects.get(id=1)
        serializer = DireccionCreateSerializer(instance=direccion_creada)

        response_data = response.data
        serializer_data = serializer.data

        self.assertEqual(response_data, serializer_data)
'''


'''
class ObtenerDireccionUsuarioTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.user = User.objects.create_user(username='testuser', password='password')
        self.region = Region.objects.create(nom_region='region 1')
        self.provincia = Provincia.objects.create(nom_provincia='provincia 1', region=self.region)
        self.comuna = Comuna.objects.create(nom_comuna='comuna 1', provincia=self.provincia)

        self.direccion = Direccion.objects.create(
            user=self.user,
            direccion='direccion',
            num_direccion=123,
            descripcion='',
            comuna=self.comuna
        )

    def test_obtener_direccion(self):

        request = self.factory.get(f'/direccion/{self.user.id}')
        response = direccion(request, id=self.user.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        expected_data = [
            {
                'id': self.direccion.id,
                'user': self.user.id,
                'direccion': 'direccion',
                'num_direccion': 123,
                'descripcion': '',
                'comuna': {
                    'id': self.comuna.id,
                    'nom_comuna': self.comuna.nom_comuna,
                    'provincia': {
                        'id': self.provincia.id,
                        'nom_provincia': self.provincia.nom_provincia,
                        'region': {
                            'id': self.region.id,
                            'nom_region': self.region.nom_region
                        }
                    }
                }
            }
        ]

        self.assertEqual(response.data, expected_data)
'''


'''
class OrderItemsTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.user = User.objects.create_user(username='testuser', password='password')

        # Crear una transacción de ejemplo
        self.transaccion = Transaccion.objects.create(
            user=self.user,
            buy_order='12345',
            session_id='67890',
            amount=1000,
            status='PENDING',
            card_number='1234',
            accounting_date='2023-06-29',
            transaction_date='2023-06-29',
            authorization_code='6789',
            payment_type_code='CARD',
            response_code=0,
            installments_number=1
        )

        # Crear un estado de ejemplo
        self.estado = Estado.objects.create(nom_estado='PENDING')

        self.order = Order.objects.create(
            user= self.user,
            subtotal= 1234,
            costo_despacho= 3990,
            total= 123445,
            tipo_entrega= 'despacho',
            direccion= 'direccion 1',
            fecha_entrega= '2024-07-04',
            correo= 'asd@correo.com',
            transaccion= self.transaccion,
            estado= self.estado
        )

        self.marca = Marca.objects.create(nom_marca='marca')
        self.categoria = Categoria.objects.create(nom_categoria='categoria')

        self.producto1 = Producto.objects.create(
            nombre= 'Producto Test',
            precio= 100,
            descripcion= 'Descripción del Producto Test',
            stock= 10,
            marca= self.marca,
            categoria= self.categoria,
        )

        self.producto2 = Producto.objects.create(
            nombre= 'Producto Test 2',
            precio= 100,
            descripcion= 'Descripción del Producto Test 2',
            stock= 10,
            marca= self.marca,
            categoria= self.categoria,
        )

    def test_order_item_single(self):
        # Datos del item de orden a crear
        order_item_data = {
            'order': self.order.id,  
            'producto': self.producto1.id,
            'cantidad': 2
        }

        request = self.factory.post('/order-items/', data=order_item_data)
        response = order_items(request=request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verificar que se haya creado correctamente el OrderItem en la base de datos
        self.assertTrue(OrderItem.objects.exists())

    def test_order_item_list(self):
        # Datos de lista de items de orden a crear
        order_items_data = [
            {
                'order': self.order.id,  # Esto se llenará automáticamente al crear la OrderItem
                'producto': self.producto1.id,  # Ajusta el producto según tus necesidades
                'cantidad': 3
            },
            {
                'order': self.order.id,  # Esto se llenará automáticamente al crear la OrderItem
                'producto': self.producto2.id,  # Ajusta el producto según tus necesidades
                'cantidad': 1
            }
        ]

        request = self.factory.post('/order-items/', order_items_data, many=True),
        response = order_items(request.data, list)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verificar que se hayan creado correctamente los OrderItems en la base de datos
        self.assertEqual(OrderItem.objects.count(), 2)
'''


class TransbankCreateTestCase(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()

    def test_transbank_create_success(self):
        # Datos de prueba para simular la solicitud
        transbank_data = {
            'amount': 1000,
            'buy_order': '12345',
            'session_id': '67890',
            'url': 'url'
        }
        # Simular la solicitud POST
        url = reverse('transbank-create')  # Asegúrate de tener el nombre correcto de la URL en tus URLs
        request = self.factory.post(url, json.dumps(transbank_data), content_type='application/json')

        # Mockear la respuesta de Transbank
        mock_response_data = {'token': 'mocked_token', 'response_code': 0}  # Simula la respuesta de Transbank
        mock_response = MagicMock()
        mock_response.json.return_value = mock_response_data
        with patch('requests.post', return_value=mock_response):
            response = transbank_create(request)

        # Verificar que la respuesta sea un JsonResponse con el contenido esperado
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertEqual(response_data['token'], 'mocked_token')
        self.assertEqual(response_data['response_code'], 0)

    def test_transbank_create_json_decode_error(self):
        # Simular una solicitud con datos JSON inválidos
        url = reverse('transbank-create')
        request = self.factory.post(url, '{invalid-json}', content_type='application/json')

        # Llamar a la función y verificar la respuesta
        response = transbank_create(request)

        # Verificar que la respuesta sea un JsonResponse con un mensaje de error y código 500
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.status_code, 500)
        response_data = json.loads(response.content)
        self.assertIn('error', response_data)






