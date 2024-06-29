from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from .views import get_marcas, create_marcas, get_marca, update_marca, delete_marca
from .models import Marca 
from .serializer import MarcaSerializer


# Create your tests here.
'''
class MarcaAPITests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_get_marcas(self):
       
        Marca.objects.create(nom_marca='Marca1')
        Marca.objects.create(nom_marca='Marca2')

        request = self.factory.get('/get-marcas/')
        response = get_marcas(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 2)  



class MarcaCreationAPITests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_create_marcas(self):

        marca_data = {'nom_marca': 'Marca de Prueba'}

        request = self.factory.post('/create-marca/', marca_data)
        response = create_marcas(request)

        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_201_CREATED])

        self.assertTrue('id' in response.data) 
        self.assertEqual(response.data['nom_marca'], marca_data['nom_marca']) 



class MarcaRetrieveAPITests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.marca1 = Marca.objects.create(nom_marca='Marca1')
        self.marca2 = Marca.objects.create(nom_marca='Marca2')

    def test_get_marca(self):

        marca_id = self.marca1.id

        request = self.factory.get(f'/get-marca/{marca_id}/')
        response = get_marca(request, pk=marca_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer = MarcaSerializer(instance=self.marca1) 
        self.assertEqual(response.data, serializer.data)  



class MarcaUpdateAPITests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.marca = Marca.objects.create(nom_marca='Marca Original')

    def test_update_marca(self):

        nueva_data = {'nom_marca': 'Marca Actualizada'}

        request = self.factory.put(f'/update-marca/{self.marca.id}/', nueva_data)
        response = update_marca(request, pk=self.marca.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.marca.refresh_from_db()

        self.assertEqual(self.marca.nom_marca, nueva_data['nom_marca'])

        serializer = MarcaSerializer(instance=self.marca)
        self.assertEqual(response.data, serializer.data)



class MarcaDeleteAPITests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.marca = Marca.objects.create(nom_marca='Marca a Eliminar')

    def test_delete_marca(self):

        marca_id = self.marca.id

        request = self.factory.delete(f'/delete-marca/{marca_id}/')
        response = delete_marca(request, pk=marca_id)

        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_204_NO_CONTENT])

        with self.assertRaises(Marca.DoesNotExist):
            Marca.objects.get(id=marca_id)
'''

