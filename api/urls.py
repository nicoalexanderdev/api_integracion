from django.urls import path
from . import views

urlpatterns = [
  path('get-marcas/', views.get_marcas),
  path('create-marca/', views.create_marcas),
  path('get-marca/<str:pk>/', views.get_marca),
  path('update-marca/<str:pk>/', views.update_marca),
  path('delete-marca/<str:pk>/', views.delete_marca),
  path('', views.get_productos),
  path('create-producto/', views.create_producto),
  path('get-producto/<int:pk>/', views.get_producto),
  path('update-producto/<str:pk>/', views.update_producto),
  path('delete-producto/<int:pk>/', views.delete_producto),
  path('get-productos-categoria/<str:pk>/', views.get_productos_categoria),
  path('get-productos-marca/<str:pk>/', views.get_productos_marca),
  path('create-categoria/', views.create_categoria),
  path('get-categorias/', views.get_categorias),
  path('update-categoria/<str:pk>/', views.update_categoria),
  path('get-categoria/<str:pk>/', views.get_categoria),
  path('delete-categoria/<str:pk>/', views.delete_categoria),
  path('buscar-productos', views.buscar_productos),
  path('update/stock/<int:pk>', views.update_stock_producto),
]