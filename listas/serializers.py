from rest_framework import serializers

from listas.models import Lista


class ListaSerializer(serializers.ModelSerializer):
    """
    General purpose Editorial serializer
    """
    class Meta:
        model = Lista
        fields = ('nombre', 'tablero', 'posicion',)
