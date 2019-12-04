from django.db import models

class Tablero(models.Model):
  nombre = models.CharField(max_length=200)
  descripcion = models.CharField(max_length=2000)
  fecha_de_creacion = models.DateTimeField()
  dueño = models.ForeignKey()
  favorito = models.ManyToManyField()
  visibilidad = models.CharField(max_length=300)
  miembros = models.ManyToManyField()

  def ___str__(self):
    return self.nombre

