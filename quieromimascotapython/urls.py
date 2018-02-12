
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/', include('app_aviso.urls')),
    url(r'^api/', include('app_direccion.urls')),
    url(r'^api/', include('app_mascota.urls')),
    url(r'^api/', include('app_usuario.urls')),
]
