# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics

from .serializers import UsuarioAuthSerializer, UsuarioSerializer
from .models import UsuarioAuth, Usuario
from quieromimascotapython.utils import ListCreateRelation
from app_aviso.serializers import AvisoSerializer


class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioAvisoList(ListCreateRelation):
    serializer_class = AvisoSerializer
    related_model_class = Usuario
    related_model_name = 'usuario'
    related_queryset_name = 'avisos'


class UsuarioAuthList(ListCreateRelation):
    serializer_class = UsuarioAuthSerializer
    related_model_class = Usuario
    related_model_name = 'usuario'
    related_queryset_name = 'auth'
    many = False


class AuthList(generics.ListCreateAPIView):
    queryset = UsuarioAuth.objects.all()
    serializer_class = UsuarioAuthSerializer


class AuthDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsuarioAuth.objects.all()
    serializer_class = UsuarioAuthSerializer
