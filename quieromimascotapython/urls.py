
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/', include('app_aviso.urls')),
    url(r'^api/', include('app_direccion.urls')),
    url(r'^api/', include('app_mascota.urls')),
    url(r'^api/', include('app_usuario.urls')),

    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^publicar/$', TemplateView.as_view(template_name='index.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
