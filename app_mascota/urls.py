from django.conf.urls import url
import views
urlpatterns = [
    url(r'^tipos', views.TipoList.as_view()),
    url(r'^tipos/(?P<pk>\d+)', views.TipoDetail.as_view()),
    url(r'^tipos/(?P<pk>\d+)/razas', views.TipoRazasList.as_view()),

    url(r'^razas', views.RazaList.as_view()),
    url(r'^razas/(?P<pk>\d+)', views.RazaDetail.as_view()),

    url(r'^mascotas', views.MascotaList.as_view()),
    url(r'^mascotas/(?P<pk>\d+)', views.MascotaDetail.as_view()),
]