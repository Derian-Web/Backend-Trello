from django.shortcuts import render
from rest_framework import viewsets
from listas.models import Lista
from listas.serializers import ListaSerializer


class ListaviewSet(viewsets.ModelViewSet):
  queryset = Lista.objects.all()
  serializer_class = ListaSerializer
