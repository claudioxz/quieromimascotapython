# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .serializers import *
from .models import *


class AvisoList(generics.ListAPIView):
    serializer_class = AvisoSerializer
    queryset = Aviso.objects.all()


class AvisoDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AvisoSerializer
    queryset = Aviso.objects.all()


class AvisoDesaparecidaList(generics.ListCreateAPIView):
    serializer_class = AvisoDesaparecidaSerializer
    queryset = AvisoDesaparecida.objects.all()


class AvisoDesaparecidaDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AvisoDesaparecidaSerializer
    queryset = AvisoDesaparecida.objects.all()


class AvisoAdopcionList(generics.ListCreateAPIView):
    serializer_class = AvisoAdopcionSerializer
    queryset = AvisoAdopcion.objects.all()


class AvisoAdopcionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AvisoAdopcionSerializer
    queryset = AvisoAdopcion.objects.all()


class AvisoEncontradaList(generics.ListCreateAPIView):
    serializer_class = AvisoEncontradaSerializer
    queryset = AvisoEncontrada.objects.all()


class AvisoEncontradaDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AvisoEncontradaSerializer
    queryset = AvisoEncontrada.objects.all()


class ImagenList(generics.ListCreateAPIView):
    serializer_class = ImagenSerializer
    queryset = Imagen.objects.all()


class ImagenDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImagenSerializer
    queryset = Imagen.objects.all()