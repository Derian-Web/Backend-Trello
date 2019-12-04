from rest_framework import serializers
from comentarios.models import Comentarios


class ComentariosSerializer(serializers.ModelSerializer):

  class Meta:
    model = Comentarios
    fields = ('tarjeta', 'mensaje', 'dueño', 'fecha_de_creacion')
