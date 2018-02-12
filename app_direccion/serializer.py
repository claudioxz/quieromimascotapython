from rest_framework import serializers
from .models import Region, Comuna, Direccion
from app_usuario.models import Usuario

class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ('id', 'nombre', 'comunas')


class ComunaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comuna
        fields = ('id', 'nombre')


class DireccionSerializer(serializers.ModelSerializer):

    comuna = serializers.PrimaryKeyRelatedField(many=False, queryset=Comuna.objects.all())
    usuario = serializers.PrimaryKeyRelatedField(many=False, queryset=Usuario.objects.all())

    class Meta:
        model = Direccion
        fields = ('id', 'comuna', 'usuario')