from rest_framework import serializers
from .models import Region, Comuna, Direccion, Provincia
from app_usuario.models import Usuario


class ComunaSerializer(serializers.ModelSerializer):

    provincia = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset=Provincia.objects.all())

    class Meta:
        model = Comuna
        fields = ('id', 'nombre', 'codigo', 'provincia')


class ProvinciasSerializer(serializers.ModelSerializer):

    region = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset=Region.objects.all())

    class Meta:
        model = Provincia
        fields = ('id', 'nombre', 'region')


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ('id', 'nombre', 'numero')


class DireccionSerializer(serializers.ModelSerializer):

    comuna = serializers.PrimaryKeyRelatedField(many=False, queryset=Comuna.objects.all())
    usuario = serializers.PrimaryKeyRelatedField(many=False, queryset=Usuario.objects.all())

    class Meta:
        model = Direccion
        fields = ('id', 'comuna', 'usuario')