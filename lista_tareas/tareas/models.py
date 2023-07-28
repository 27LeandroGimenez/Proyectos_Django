from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tarea(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    completado = models.BooleanField(default=False, verbose_name="Completada: ")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['completado']