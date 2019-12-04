from rest_framework import serializers
from tarjetas.models import Tarjeta


class TarjetaSerializer(serializers.ModelSerializer):

  class Meta:
    model = Tarjeta
    fields = ('nombre', 'lista', 'descripcion', 'miembros', 'dueño', 'fecha_de_creacion', 'fecha_de_vencimiento ', 'entero')
