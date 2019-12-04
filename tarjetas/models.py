from django.db import models

# Create your models here.

class Tarjeta(models.Model):
  nombre = models.CharField(max_length=200)
  lista = models.ForeignKey()
  descripcion = models.CharField(max_length=200)
  miembros = models.ManyToManyField()
  dueño = models.ForeignKey()
  fecha_de_creacion = models.DateTimeField()
  fecha_de_vencimiento = models.DateTimeField()
  entero = models.IntegerField()

  def __str__(self):
    return self.nombre
