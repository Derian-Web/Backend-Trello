from django.shortcuts import render
from rest_framework import viewsets
from comentarios.models import Comentarios
from comentarios.serializers import ComentariosSerializer


class ComentariosViewSet(viewsets.ModelViewSet):
    """
    Editorial endpoint (viewset)
    """
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer
