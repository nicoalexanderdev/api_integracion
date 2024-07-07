from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/productos/', include('api.urls')),
    path('api/accounts/', include('user.urls')),
    path('api/compras/', include('compra.urls')),
    path('api/token/', obtain_auth_token), 
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
