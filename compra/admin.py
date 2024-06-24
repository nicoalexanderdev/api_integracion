from django.contrib import admin
from .models import Transaccion, Region, Provincia, Comuna, Direccion

# Register your models here.

admin.site.register(Transaccion)
admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)
admin.site.register(Direccion)