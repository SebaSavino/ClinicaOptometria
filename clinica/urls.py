from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
    path('pacientes/', include('pacientes.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('reportes/', include('reportes.urls')),
    path('', include('compartido.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
