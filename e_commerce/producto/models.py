from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = 'Categorias'

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='imagen_productos', blank=True, null=True)
    vendido = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    #permite saber el usuario que creo el producto, y tambien obtener informacion de los productos asociados al usuario.
    usuario = models.ForeignKey(User, related_name='productos', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} - ${self.precio} - {self.categoria}'

class Carrito(models.Model):
    #carrito pertence a un unico usuario y no puede estar asociado a mas de uno
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)