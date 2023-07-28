from django.urls import path
from .views import *

urlpatterns = [
    path('', TareasListView.as_view(), name='index'),
    path('crear_tarea/', TareaCreateView.as_view(), name='crear-tarea'),
    path('actualizar_tarea/<pk>/', TareaUpdateView.as_view(), name='actualizar-tarea'),
    path('eliminar_tarea/<pk>/', TareaDeleteView.as_view(), name='eliminar-tarea'),
]
