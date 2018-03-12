from django.conf.urls import url
import views

urlpatterns = [
    url(r'^usuarios$', views.UsuarioList.as_view()),
    url(r'^usuarios/(?P<pk>\d+)$', views.UsuarioDetail.as_view()),
    url(r'^usuarios/(?P<pk>\d+)/auth$', views.UsuarioAuthList.as_view()),
    url(r'^usuarios/(?P<pk>\d+)/avisos$', views.UsuarioAvisoList.as_view()),

    url(r'^auth$', views.AuthList.as_view()),
    url(r'^auth/(?P<pk>\d+)$', views.AuthList.as_view()),
]
