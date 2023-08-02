from django.urls import path
from .views import *

urlpatterns = [
    path('', EmpleadosListView.as_view(), name='lista-empleados'),
    path('crear_empleado/', EmpleadoCreateView.as_view(), name='crear-empleado'),
    path('actualizar_empleado/<int:pk>/', EmpleadoUpdateView.as_view(), name='actualizar-empleado'),
    path('eliminar_empleado/<int:pk>/', EmpleadoDeleteView.as_view(), name='eliminar-empleado'),
]
