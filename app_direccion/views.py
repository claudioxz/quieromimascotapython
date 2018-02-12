# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics

from .serializer import DireccionSerializer, ComunaSerializer, RegionSerializer
from .models import Comuna, Direccion, Region
from quieromimascotapython.utils import ListCreateRelation


class RegionList(generics.ListCreateAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class RegionComunaList(ListCreateRelation):
    related_queryset_name = 'comunas'
    related_model_name = 'region'
    related_model_class = Region
    serializer_class = ComunaSerializer


class ComunaList(generics.ListCreateAPIView):
    serializer_class = ComunaSerializer
    queryset = Comuna.objects.all()


class ComunaDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ComunaSerializer
    queryset = Comuna.objects.all()


class DireccionList(generics.ListCreateAPIView):
    serializer_class = DireccionSerializer
    queryset = Direccion.objects.all()


class DireccionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DireccionSerializer
    queryset = Direccion.objects.all()



