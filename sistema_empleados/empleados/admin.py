from django.contrib import admin
from .models import Empleado

# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']

admin.site.register(Empleado, EmpleadoAdmin)