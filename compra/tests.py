
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from .views import region, provincia, direccion, agregar_direccion, crear_orden_compra, order_items, transbank_create, transbank_commit
from .models import Region, Provincia, Comuna, Direccion, Transaccion, Estado, Order
from .serializer import ProvinciaSerializer, DireccionCreateSerializer, OrderSerializer 
from django.contrib.auth.models import User
from api.models import Producto, Marca, Categoria
import json
import responses

# Create your tests here.

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




class OrderItemAPITests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.transaccion = Transaccion.objects.create(
            user=self.user, buy_order='12345678', session_id='abc123', amount=10000, 
            status='AUTHORIZED', card_number='1234', accounting_date='2023-01-01', 
            transaction_date='2023-01-01', authorization_code='000000', 
            payment_type_code='VD', response_code=0, installments_number=1)
        self.estado = Estado.objects.create(nom_estado='Pendiente')
        self.order = Order.objects.create(
            user=self.user, subtotal=10000, costo_despacho=500, total=10500, 
            tipo_entrega='Envio', direccion='123 Fake St', fecha_entrega='2023-01-01', 
            correo='testuser@example.com', transaccion=self.transaccion, estado=self.estado)
        self.producto = Producto.objects.create(
            nombre='Producto Test', precio=1000, descripcion='Descripción del Producto Test',
            stock=100, marca=Marca.objects.create(nom_marca='Marca Test'), 
            categoria=Categoria.objects.create(nom_categoria='Categoría Test'))

    def test_create_single_order_item(self):
        order_item_data = {
            'order': self.order.id,
            'producto': self.producto.id,
            'cantidad': 5
        }
        request = self.factory.post('/order-items/', order_item_data, format='json')
        response = order_items(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['order'], self.order.id)
        self.assertEqual(response.data['producto'], self.producto.id)
        self.assertEqual(response.data['cantidad'], 5)
        
    def test_create_multiple_order_items(self):
        order_items_data = [
            {
                'order': self.order.id,
                'producto': self.producto.id,
                'cantidad': 2
            },
            {
                'order': self.order.id,
                'producto': self.producto.id,
                'cantidad': 3
            }
        ]
        request = self.factory.post('/order-items/', json.dumps(order_items_data), content_type='application/json')
        response = order_items(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['cantidad'], 2)
        self.assertEqual(response.data[1]['cantidad'], 3)




class TransbankCreateAPITests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    @responses.activate
    def test_transbank_create(self):
        # Simula la respuesta de Transbank
        transbank_response = {
            'token': 'fake_token',
            'url': 'https://fakeurl.com'
        }
        responses.add(
            responses.POST,
            'https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions',
            json=transbank_response,
            status=200
        )

        # Datos de prueba para enviar en la solicitud POST
        request_data = {
            'buy_order': '12345678',
            'session_id': 'abc123',
            'amount': 10000,
            'return_url': 'https://www.return.url'
        }
        
        # Crea una solicitud POST simulada a la vista transbank_create
        request = self.factory.post('/transaction/create/', json.dumps(request_data), content_type='application/json')

        # Invoca la función transbank_create con la solicitud simulada
        response = transbank_create(request)

        # Verifica que la respuesta sea HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica que los datos devueltos por Transbank sean correctos
        response_data = json.loads(response.content)
        self.assertEqual(response_data, transbank_response)

        # Verifica que la solicitud a Transbank se haya realizado correctamente
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.url, 'https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions')
        self.assertEqual(json.loads(responses.calls[0].request.body), request_data)




class TransbankCommitAPITests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    @responses.activate
    def test_transbank_commit(self):
        # Simula la respuesta de Transbank
        tokenws = "fake_tokenws"
        transbank_response = {
            'status': 'AUTHORIZED',
            'amount': 10000,
            'buy_order': '12345678',
            'session_id': 'abc123'
        }
        responses.add(
            responses.PUT,
            f'https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{tokenws}',
            json=transbank_response,
            status=200
        )

        # Crea una solicitud PUT simulada a la vista transbank_commit
        request = self.factory.put(f'/commit/{tokenws}/')

        # Invoca la función transbank_commit con la solicitud simulada
        response = transbank_commit(request, tokenws=tokenws)

        # Verifica que la respuesta sea HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica que los datos devueltos por Transbank sean correctos
        response_data = json.loads(response.content)
        self.assertEqual(response_data, transbank_response)

        # Verifica que la solicitud a Transbank se haya realizado correctamente
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.url, f'https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{tokenws}')





