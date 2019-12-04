from django.shortcuts import render

from rest_framework import viewsets
from tableros.models import Tablero
from tableros.serializers import TableroSerializer


class tablerosviewSet(viewsets.ModelViewSet):
  queryset = Tablero.objects.all()
  serializer_class = TableroSerializer
