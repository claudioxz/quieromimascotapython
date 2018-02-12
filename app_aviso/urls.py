from django.conf.urls import url
import views
urlpatterns = [
    url(r'^avisos$', views.AvisoList.as_view()),
    url(r'^avisos/(?P<pk>\d+)$', views.AvisoDetails.as_view()),

    url(r'^aviso_desaparecidas$', views.AvisoDesaparecidaList.as_view()),
    url(r'^aviso_desaparecidas/(?P<pk>\d+)$', views.AvisoDesaparecidaDetails.as_view()),

    url(r'^aviso_adopciones$', views.AvisoAdopcionList.as_view()),
    url(r'^aviso_adopciones/(?P<pk>\d+)$', views.AvisoAdopcionDetail.as_view()),

    url(r'^aviso_encontradas$', views.AvisoEncontradaList.as_view()),
    url(r'^aviso_encontradas/(?P<pk>\d+)$', views.AvisoEncontradaDetail.as_view()),

    url(r'^imagenes/$', views.ImagenList.as_view()),
    url(r'^imagenes/(?P<pk>\d+)$', views.ImagenDetail.as_view()),

]
