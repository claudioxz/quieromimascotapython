from rest_framework import serializers
from .models import Mascota, Tipo, Raza


class TipoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tipo
        fields = ('id', 'nombre', 'razas')


class RazaSerializer(serializers.ModelSerializer):
    tipo = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset=Tipo.objects.all())

    class Meta:
        model = Raza
        fields = ('id', 'nombre', 'tipo')


class MascotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mascota
        fields = ('id', 'genero', 'nombre', 'edad', 'raza')