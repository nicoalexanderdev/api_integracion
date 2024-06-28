from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from django.http import JsonResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt

from djangoconfig import settings
from .serializer import  ProvinciaSerializer, TransaccionSerializer, DireccionSerializer, RegionSerializer, ComunaSerializer, DireccionCreateSerializer, SucursalSerializer, OrderSerializer, OrderItemSerializer, GetOrdersSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Region, Provincia, Comuna, Direccion, Sucursal, Carro, CarroItem, Order, OrderItem
from datetime import date
from django.contrib.auth.models import User
from api.models import Producto

# Create your views here.


@api_view(['GET'])
def buy_orders(request):
    orders = Order.objects.all()
    serializer = GetOrdersSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def order_items(request):
    if isinstance(request.data, list):
        serializer = OrderItemSerializer(data=request.data, many=True, context={'request': request})
    else:
        serializer = OrderItemSerializer(data=request.data, context={'request': request})

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def crear_orden_compra(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return 201 Created on success
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def sucursal(request):
    sucursales =Sucursal.objects.all()
    serializer = SucursalSerializer(sucursales, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def comuna(request, id):
    try:
        provincia = get_object_or_404(Provincia, id=id)
        comunas = Comuna.objects.filter(provincia=provincia)
        serializer = ComunaSerializer(comunas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def provincia(request, id):
    try:
        region = get_object_or_404(Region, id=id)
        provincias = Provincia.objects.filter(region=region)
        serializer = ProvinciaSerializer(provincias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def region(request):
    regiones = Region.objects.all()
    serializer = RegionSerializer(regiones, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def direccion(request, id):
    try:
        user = get_object_or_404(User, id=id)
        direcciones = Direccion.objects.filter(user=user)
        serializer = DireccionSerializer(direcciones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])
def agregar_direccion(request):
    try:
        print(f'Datos recibidos en POST: {request.data}')
        serializer = DireccionCreateSerializer(data=request.data)
        if serializer.is_valid():
            direccion = serializer.save()
            return Response(DireccionSerializer(direccion).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    



def headers_request_transbank():
    headers = {  # DEFINICIÓN TIPO DE AUTORIZACIÓN Y AUTENTICACIÓN
        "Authorization": "Token",
        # LLAVE QUE DEBE SER MODIFICADA PORQUE ES SOLO DEL AMBIENTE DE INTEGRACIÓN DE TRANSBANK (PRUEBAS)
        "Tbk-Api-Key-Id": "597055555532",
        # LLAVE QUE DEBE SER MODIFICADA PORQUE DEL AMBIENTE DE INTEGRACIÓN DE TRANSBANK (PRUEBAS)
        "Tbk-Api-Key-Secret": "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C",
        # DEFINICIÓN DEL TIPO DE INFORMACIÓN ENVIADA
        "Content-Type": "application/json",
        # DEFINICIÓN DE RECURSOS COMPARTIDOS ENTRE DISTINTOS SERVIDORES PARA CUALQUIER MÁQUINA
        "Access-Control-Allow-Origin": "*",
        'Referrer-Policy': 'origin-when-cross-origin',
    }
    return headers


@api_view(['POST'])
def transbank_create(request):
    try:
        # LECTURA DEL PAYLOAD (BODY) CON INFORMACIÓN DE TIPO JSON
        print('headers: ', request.headers)
        data = json.loads(request.body)
        print('data: ', data)

        # DEFINICIÓN DE URL DE TRANSBANK PARA CREAR UNA TRANSACCIÓN
        url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions"

        # CABECERA SOLICITADA POR TRANSBANK
        headers = headers_request_transbank()

        # INVOCACIÓN POR POST A API REST QUE CREA UNA TRANSACCIÓN EN TRANSBANK
        response = requests.post(url, json=data, headers=headers)
        print('response: ', response.json())

        # RETORNO DE LA RESPUESTA DE TRANSBANK
        return JsonResponse(response.json())

    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Error de decodificación JSON: {}'.format(str(e))}, status=500)


@csrf_exempt
@api_view(['PUT'])
def transbank_commit(request, tokenws):
    try:
        print('tokenws: ', tokenws)

        # FORMACIÓN DE LA URL DE TRANSBANK PARA CONFIRMAR UNA TRANSACCIÓN
        url = f"https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{tokenws}"

        # CABECERA SOLICITADA POR TRANSBANK
        headers = headers_request_transbank()

        # INVOCACIÓN POR PUT A API REST QUE CONFIRMA UNA TRANSACCIÓN EN TRANSBANK
        response = requests.put(url, headers=headers)
        response_data = response.json()
        print('response: ', response_data)

        # RETORNO DE LA RESPUESTA DE TRANSBANK
        return JsonResponse(response_data, safe=False)

    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Error de decodificación JSON: {}'.format(str(e))}, status=500)
    except Exception as e:
        # Manejar cualquier excepción que pueda ocurrir durante la solicitud a la API de Transbank
        print(f"Error al confirmar transacción en Transbank: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['GET'])
def transbank_get_status(request, tokenws):
    try:
        print('tokenws: ', tokenws)

        # FORMACIÓN DE LA URL DE TRANSBANK PARA CONFIRMAR UNA TRANSACCIÓN
        url = f"https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{tokenws}"

        # CABECERA SOLICITADA POR TRANSBANK
        headers = headers_request_transbank()

        # INVOCACIÓN POR GET A API REST QUE CONFIRMA UNA TRANSACCIÓN EN TRANSBANK
        response = requests.get(url, headers=headers)
        print('response: ', response.json())

        # RETORNO DE LA RESPUESTA DE TRANSBANK
        return JsonResponse(response.json())

    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Error de decodificación JSON: {}'.format(str(e))}, status=500)


@api_view(['POST'])
def transbank_reverse_or_cancel(request, tokenws):
    try:
        print('tokenws: ', tokenws)

        # LECTURA DEL PAYLOAD (BODY) CON INFORMACIÓN DE TIPO JSON
        data = json.loads(request.body)
        print('data: ', data)

        # FORMACIÓN DE LA URL DE TRANSBANK PARA CANCELAR UNA TRANSACCIÓN
        url = f"https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{tokenws}/refunds"

        # CABECERA SOLICITADA POR TRANSBANK
        headers = headers_request_transbank()

        # INVOCACIÓN POR POST A API REST QUE CANCELA UNA TRANSACCIÓN EN TRANSBANK
        response = requests.post(url, json=data, headers=headers)
        print('response: ', response.json())

        # RETORNO DE LA RESPUESTA DE TRANSBANK
        return JsonResponse(response.json())

    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Error de decodificación JSON: {}'.format(str(e))}, status=500)


@api_view(['PUT'])
def transbank_capture(request, tokenws):
    try:
        url = f"https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{tokenws}/capture"

        headers = headers_request_transbank()
        response = requests.put(url, headers=headers)
        response_data = response.json()
        print('response: ', response_data)  

        return JsonResponse(response_data, safe=False)

    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Error de decodificación JSON: {}'.format(str(e))}, status=500)
    except Exception as e:
        # Manejar cualquier excepción que pueda ocurrir durante la solicitud a la API de Transbank
        print(f"Error al confirmar transacción en Transbank: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['POST'])
def transaction_save(request):
    serializer = TransaccionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'transaction': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_dollar_value(request):
    try:
        user = settings.USER_BCN
        password = settings.PASS_BCN
        timeseries = 'F073.TCO.PRE.Z.D'
        firstdate = '2024-05-19'
        lastdate = date.today().strftime('%Y-%m-%d')

        url = f'{settings.API_BCN_CENTRAL}user={user}&pass={password}&timeseries={timeseries}&firstdate={firstdate}&lastdate={lastdate}'

        response = requests.get(url)
        response.raise_for_status()
        dolar = response.json()


        # Obtener el valor del día actual
        today_value = None
        for obs in dolar.get('Series', {}).get('Obs', []):
            if obs.get('indexDateString') == lastdate:
                value = obs.get('value')
                if value and value.lower() != 'nan':
                    today_value = value
                    break

        # Si el valor del día actual es NaN, buscar el último valor no NaN en las observaciones
        if today_value is None or today_value.lower() == 'nan':
            observations = dolar.get('Series', {}).get('Obs', [])
            for obs in reversed(observations):
                value = obs.get('value')
                if value and value.lower() != 'nan':
                    today_value = value
                    break

        if today_value is None or today_value.lower() == 'nan':
            raise ValueError("No se encontró un valor válido para el dólar.")

        return Response({'value': today_value})
    except Exception as e:
        print(f"Error al obtener valor del dolar: {e}")
        return JsonResponse({'error': str(e)}, status=500)
