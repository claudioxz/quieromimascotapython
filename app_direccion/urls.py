from django.conf.urls import url
import views

urlpatterns = [
    url(r'^regiones', views.RegionList.as_view()),
    url(r'^regiones/(?P<pk>\d+)', views.RegionDetail.as_view()),
    url(r'^regiones/(?P<pk>\d+)/comunas', views.RegionComunaList.as_view()),

    url(r'^comunas', views.ComunaList.as_view()),
    url(r'^comunas/(?P<pk>\d+)', views.ComunaDetail.as_view()),

    url(r'^direcciones', views.DireccionList.as_view()),
    url(r'^direcciones/(?P<pk>\d+)', views.DireccionDetail.as_view()),
]