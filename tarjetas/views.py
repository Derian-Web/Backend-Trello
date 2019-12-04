from django.shortcuts import render
from rest_framework import viewsets
from tarjetas.models import Tarjeta
from tarjetas.serializers import TarjetaSerializer


class TarjetaViewSet(viewsets.ModelViewSet):
    """
    Editorial endpoint (viewset)
    """
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer
