from django.conf.urls import url
import views
urlpatterns = [
    url(r'^insertar_todo$', views.insertar_region_provincia_comuna),

    url(r'^regiones$', views.RegionList.as_view()),
    url(r'^regiones/(?P<pk>\d+)$', views.RegionDetail.as_view()),
    url(r'^regiones/(?P<pk>\d+)/provincias$', views.RegionProvinciaList.as_view()),

    url(r'^provincias$', views.ProvinciaList.as_view()),
    url(r'^provincias/(?P<pk>\d+)$', views.ProvinciaDetail.as_view()),
    url(r'^provincias/(?P<pk>\d+)/comunas$', views.ProvinciaComunasList.as_view()),

    url(r'^comunas$', views.ComunaList.as_view()),
    url(r'^comunas/(?P<pk>\d+)$', views.ComunaDetail.as_view()),

    url(r'^direcciones$', views.DireccionList.as_view()),
    url(r'^direcciones/(?P<pk>\d+)$', views.DireccionDetail.as_view()),
]

