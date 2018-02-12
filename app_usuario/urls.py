from django.conf.urls import url
import views

urlpatterns = [
    url(r'^usuarios$', views.UsuarioList.as_view()),
    url(r'^usuarios/(?P<pk>\d+)$', views.UsuarioDetail.as_view()),

    url(r'^usuarios_auth$', views.UsuarioAuthList.as_view()),
    url(r'^usuarios_auth/(?P<pk>\d+)$', views.UsuarioAuthDetail.as_view()),
]
