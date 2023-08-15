from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .models import Categoria, Producto, Carrito, ItemCarrito

# Create your views here.

class Inicio(ListView):
    model = Producto
    template_name = 'producto/index.html'
    context_object_name = 'productos'

    #filtrar los productos
    def get_queryset(self):
        categoria = self.request.GET.get('categoria')
        if categoria is None:
            queryset = Producto.objects.filter(vendido=False)
        else:
            queryset = Producto.objects.filter(categoria__nombre=categoria)
        return queryset
    
    #contexto para obtener todas las categorias
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()

        kword = self.request.GET.get('kword')
        if kword:
            context['productos'] = Producto.objects.filter(nombre__icontains=kword)
        return context

class ProductoCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Producto
    template_name = 'producto/crear_producto.html'
    fields = ['categoria', 'nombre', 'descripcion', 'precio', 'imagen', 'vendido',]
    success_url = reverse_lazy('inicio')
    success_message = 'Producto creado exitosamente.'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
class ProductoUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = 'producto/actualizar_producto.html'
    fields = ['categoria', 'nombre', 'descripcion', 'precio', 'imagen', 'vendido',]
    success_url = reverse_lazy('inicio')
    success_message = 'Producto actualizado exitosamente.'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class ProductoDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'producto/eliminar_producto.html'
    success_url = reverse_lazy('inicio')
    success_message = 'Producto eliminado exitosamente.'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


def agregar_al_carrito(request, producto_id):
    producto, creado = Producto.objects.get_or_create(pk=producto_id)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    item, creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    
    if creado:
        # Si el item ya estaba en el carrito, no hagas nada
        pass
    else:
        # Si el item no estaba en el carrito, crea un nuevo item
        item.cantidad = 1
        item.save()

    return redirect('carrito')


def pagina_del_carrito(request):
    carrito = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.items.all() if isinstance(carrito, Carrito) else []
    
    total_carrito = 0

    for item in items:
        item.subtotal = item.cantidad * item.producto.precio
        total_carrito += item.subtotal
    
    return render(request, 'producto/carrito.html', {'items': items, 'total':total_carrito})