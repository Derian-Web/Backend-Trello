from rest_framework import serializers
from tableros.models import Tablero


class TableroSerializer(serializers.ModelSerializer):

  class Meta:
    model = Tablero
    fields = ('nombre', ' descripcion ', 'fecha_de_creacion', 'dueño', 'favorito', 'visibilidad', 'miembros')
