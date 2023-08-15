from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
    path('crear_producto/', ProductoCreateView.as_view(), name='crear-producto'),
    path('actualizar_producto/<int:pk>/', ProductoUpdateView.as_view(), name='actualizar-producto'),
    path('eliminar_producto/<int:pk>/', ProductoDeleteView.as_view(), name='eliminar-producto'),
    path('agregar_carrito/<int:producto_id>/', agregar_al_carrito, name='agregar-al-carrito'),
    path('carrito/', pagina_del_carrito, name='carrito'),
]
