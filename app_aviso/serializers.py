from rest_framework import serializers
from .models import *


class AvisoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aviso
        fields = ('descripcion', 'titulo', 'fecha_publicacion', 'tipo_aviso')

    def get_tipo_aviso(self, aviso):
        return {'tipo_aviso': ['', '']}


class AvisoAdopcionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AvisoAdopcion
        fields = ('descripcion', 'titulo', 'fecha_publicacion', 'tipo_aviso', 'mascota')


class AvisoDesaparecidaSerializer(serializers.ModelSerializer):

    mascota = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = AvisoDesaparecida
        fields = ('descripcion', 'titulo', 'fecha_publicacion', 'tipo_aviso',
                  'mascota', 'fecha_desaparecida', 'lugar')


class AvisoEncontradaSerializer(serializers.ModelSerializer):

    class Meta:
        model = AvisoEncontrada
        fields = ('descripcion', 'titulo', 'fecha_publicacion', 'tipo_aviso',
                  'fecha_encontrada', 'lugar')


class ImagenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Imagen
        fields = ('archivo',)
