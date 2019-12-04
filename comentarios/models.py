from django.db import models

# Create your models here.

class Comentarios(models.Model):
  tarjeta = models.ForeignKey()
  mensaje = models.CharField(max_length=200)
  dueño = models.ForeignKey()
  fecha_de_creacion = models.DateTimeField()
