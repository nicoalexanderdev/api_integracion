from django.urls import path
from . import views

urlpatterns = [
  path('get-marcas', views.get_marcas),
  path('create-marcas', views.create_marcas),
  path('get-productos', views.get_productos),
  path('create-producto', views.create_producto),
]