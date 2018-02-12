# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from quieromimascotapython.utils import ListCreateRelation
from .models import Mascota, Tipo, Raza
from .serializers import MascotaSerializer, RazaSerializer, TipoSerializer


class TipoList(generics.ListCreateAPIView):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer


class TipoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer


class TipoRazasList(ListCreateRelation):
    related_queryset_name = 'razas'
    related_model_class = Raza
    related_model_name = 'tipo'
    serializer_class = RazaSerializer


class RazaList(generics.ListCreateAPIView):
    queryset = Raza.objects.all()
    serializer_class = RazaSerializer


class RazaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Raza.objects.all()
    serializer_class = RazaSerializer


class MascotaList(generics.CreateAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer


class MascotaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
