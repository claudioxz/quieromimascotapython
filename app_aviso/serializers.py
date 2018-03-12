from rest_framework import serializers
from .models import *
from app_mascota.serializers import MascotaSerializer


class ImagenSerializer(serializers.ModelSerializer):

    aviso = serializers.PrimaryKeyRelatedField(queryset=Aviso.objects.all(), write_only=True)

    class Meta:
        model = Imagen
        fields = ('id', 'archivo', 'aviso')


class AvisoSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(many=False, queryset=Usuario.objects.all())
    imagenes = ImagenSerializer(many=True, required=False)
    tipo_aviso = serializers.DictField(source="get_tipo_aviso")

    def update(self, instance, validated_data):
        usuario_id = validated_data.pop('usuario')
        usuario = Usuario.objects.get(usuario_id)
        imagenes_data = validated_data.pop('imagenes')

        instance.usuario = usuario

        for attr, value in validated_data.items():
            field = getattr(instance, attr)
            field.set(value)

        self.create_images(imagenes_data, instance)
        instance.save()
        return instance

    def create(self, validated_data):
        imagenes_data = validated_data.pop('imagenes')
        tipo_aviso = validated_data.get('tipo_aviso')

        options = {
            1: lambda data: AvisoAdopcion.objects.create(**data),
            2: lambda data: AvisoAdoptar.objects.create(**data),
            3: lambda data: AvisoDesaparecida.objects.create(**data),
            4: lambda data: AvisoEncontrada.objects.create(**data),
        }

        aviso = options[tipo_aviso](validated_data)
        self.create_images(imagenes_data, aviso)
        return aviso

    def create_images(self, imagenes_data, aviso):
        for imagen_data in imagenes_data:
            Imagen.objects.create(aviso=aviso, **imagen_data)

    class Meta:
        model = Aviso
        fields = ('id', 'usuario', 'descripcion', 'titulo',
                  'fecha_publicacion', 'tipo_aviso', 'imagenes')


class AvisoAdopcionSerializer(AvisoSerializer):
    mascota = MascotaSerializer(many=False, )

    def create(self, validated_data):
        mascota_data = validated_data.pop('mascota')
        mascota = Mascota.objects.create(**mascota_data)
        validated_data.update({'mascota': mascota})
        aviso = super(AvisoAdopcionSerializer, self).create(validated_data)
        return aviso

    class Meta:
        model = AvisoAdopcion
        fields = AvisoSerializer.Meta.fields+('mascota',)


class AvisoAdoptarSerializer(AvisoSerializer):
    mascota = MascotaSerializer(many=False, )

    def create(self, validated_data):
        mascota_data = validated_data.pop('mascota')
        mascota = Mascota.objects.create(**mascota_data)
        validated_data.update({'mascota': mascota})
        aviso = super(AvisoAdoptarSerializer, self).create(validated_data)
        return aviso

    class Meta:
        model = AvisoAdoptar
        fields = AvisoSerializer.Meta.fields+('mascota',)


class AvisoDesaparecidaSerializer(AvisoSerializer):
    mascota = MascotaSerializer(many=False, )

    def create(self, validated_data):
        mascota_data = validated_data.pop('mascota')
        mascota = Mascota.objects.create(**mascota_data)
        validated_data.update({'mascota': mascota})
        aviso = super(AvisoDesaparecidaSerializer, self).create(validated_data)
        return aviso

    class Meta:
        model = AvisoDesaparecida
        fields = AvisoSerializer.Meta.fields+('mascota', 'fecha_desaparecida', 'lugar')


class AvisoEncontradaSerializer(AvisoSerializer):
    class Meta:
        model = AvisoEncontrada
        fields = AvisoSerializer.Meta.fields+('fecha_encontrada', 'lugar')

