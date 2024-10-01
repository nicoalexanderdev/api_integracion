from django.urls import path
from . import views

urlpatterns = [
    path('transactions/create', views.transbank_create),
    path('transactions/<str:tokenws>/reverse-cancel',
         views.transbank_reverse_or_cancel),
    path('transactions/<str:tokenws>/commit', views.transbank_commit),
    path('transactions/<str:tokenws>/status', views.transbank_get_status),
    path('transactions/<str:tokenws>/capture', views.transbank_capture),
    path('transactions/save', views.transaction_save),
    path('foreign-exchange/usd', views.get_dollar_value),
    path('address', views.agregar_direccion),
    path('region', views.region),
    path('provincia/region/<str:id>', views.provincia),
    path('comuna/provincia/<str:id>', views.comuna),
    path('address/user/<int:id>', views.direccion),
    path('sucursales', views.sucursal),
    path('buy-orders/create', views.crear_orden_compra),
    path('buy-orders/items', views.order_items),
    path('buy-orders', views.get_estado_query),
    path('buy-orders/<str:pk>/status', views.update_order_status),
    path('buy-orders/<str:pk>', views.get_order),
    path('transactions', views.get_transactions),
    path('cart/add', views.add_to_cart),
    path('cart/items/<str:item_id>', views.remove_from_cart),
    path('cart/items/<str:item_id>/', views.update_cart_item),
    path('cart/details', views.cart_detail),
    path('cart/clear', views.clear_cart)
]
