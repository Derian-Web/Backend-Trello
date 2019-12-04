from django.db import models

class Usuario(models.Model):
  nombre = models.CharField(max_length=200)
  apellidos = models.CharField(max_length=200)
  correo = models.EmailField(max_length=200)
  contraseña = models.CharField(max_length=20)

  def ___str__(self):
    return self.nombre
