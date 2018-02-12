# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .serializers import UsuarioAuthSerializer, UsuarioSerializer
from .models import UsuarioAuth, Usuario

from rest_framework import generics


class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioAuthList(generics.ListCreateAPIView):
    queryset = UsuarioAuth.objects.all()
    serializer_class = UsuarioAuthSerializer


class UsuarioAuthDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsuarioAuth.objects.all()
    serializer_class = UsuarioAuthSerializer
