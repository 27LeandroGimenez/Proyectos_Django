from django.db import models

# Create your models here.

class Empleado(models.Model):
    HOMBRE = 'H'
    MUJER = 'M'
    GENERO = [
        (HOMBRE, 'Hombre'),
        (MUJER, 'Mujer'),
    ]

    nombre_completo = models.CharField(max_length=255)
    telefono = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField()
    edad = models.PositiveIntegerField()
    genero = models.CharField(max_length=1, choices=GENERO)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.nombre_completo} + {self.genero}'
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'