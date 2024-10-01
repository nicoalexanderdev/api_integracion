from django.urls import path
from . import views

urlpatterns = [
    path('makers', views.get_marcas),
    path('makers', views.create_marcas),
    path('makers/<str:pk>', views.get_marca),
    path('makers/<str:pk>', views.update_marca),
    path('makers/<str:pk>', views.delete_marca),
    path('products', views.get_productos),
    path('products', views.create_producto),
    path('products/<str:pk>', views.get_producto),
    path('products/<str:pk>', views.update_producto),
    path('products/<str:pk>', views.delete_producto),
    path('products/category/<str:pk>', views.get_productos_categoria),
    path('products/maker/<str:pk>', views.get_productos_marca),
    path('categories', views.get_categorias),
    path('categories', views.create_categoria),
    path('categories/<str:pk>', views.update_categoria),
    path('categories/<str:pk>', views.get_categoria),
    path('categories/<str:pk>', views.delete_categoria),
    path('search', views.buscar_productos),
    path('products/<str:pk>/stock', views.update_stock_producto),
]
