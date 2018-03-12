# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics

from .serializer import DireccionSerializer, ComunaSerializer, RegionSerializer, ProvinciasSerializer
from .models import Comuna, Direccion, Region, Provincia
from quieromimascotapython.utils import ListCreateRelation

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def insertar_region_provincia_comuna(request):
    for region_data in request.data:
        provincias = region_data.pop('provincias')

        region_serializer = RegionSerializer(data=region_data, many=False)
        region_serializer.is_valid()
        region = region_serializer.save()
        print "lala"
        for provincia_data in provincias:
            comunas = provincia_data.pop('comunas')
            provincia_data.update({'region': region.id})

            provincia_serializer = ProvinciasSerializer(data=provincia_data, many=False)

            provincia_serializer.is_valid()
            provincia = provincia_serializer.save()

            for comuna_data in comunas:
                comuna_data.update({'provincia': provincia.id})

                comuna_serializer = ComunaSerializer(data=comuna_data, many=False)
                comuna_serializer.is_valid()
                comuna_serializer.save()

    return Response(data={'lala': 'lala'})


class RegionList(generics.ListCreateAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class RegionProvinciaList(ListCreateRelation):
    related_queryset_name = 'provincias'
    related_model_name = 'region'
    related_model_class = Region
    serializer_class = ProvinciasSerializer


class ProvinciaList(generics.ListCreateAPIView):
    serializer_class = ProvinciasSerializer
    queryset = Provincia.objects.all()


class ProvinciaDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProvinciasSerializer
    queryset = Provincia.objects.all()


class ProvinciaComunasList(ListCreateRelation):
    serializer_class = ComunaSerializer
    related_model_name = 'provinca'
    related_queryset_name = 'comunas'
    related_model_class = Provincia


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



