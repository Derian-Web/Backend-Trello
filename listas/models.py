from django.db import models

# Create your models here.
class Lista(models.Model):
  nombre = models.CharField(max_length=200)
  tablero = models.ForeignKey()
  posicion = models.IntegerField()
