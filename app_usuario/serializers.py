from rest_framework import serializers
from .models import Usuario, UsuarioAuth


class UsuarioAuthSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = UsuarioAuth
        fields = ('id', 'email', 'password', 'usuario')


class UsuarioSerializer(serializers.ModelSerializer):
    auth = UsuarioAuthSerializer(many=False)

    class Meta:
        model = Usuario
        fields = ('id', 'nombre', 'apellido', 'numero_celular',
                  'numero_fijo', 'fecha_creada', 'auth')

    def create(self, validated_data):
        auth = validated_data.pop('auth')
        usuario = Usuario.objects.create(**validated_data)
        usuario.save()
        UsuarioAuth.objects.create(usuario=usuario, **auth)
        return usuario
