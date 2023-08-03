from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Empleado
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin 

# Create your views here.

class EmpleadosListView(ListView):
    context_object_name = 'empleados'
    template_name = 'empleados/lista_empleados.html'
    paginate_by = 5

    def get_queryset(self):
        buscar_empleado = self.request.GET.get('q', '')
        lista = Empleado.objects.filter(nombre_completo__icontains=buscar_empleado)
        return lista
    
class EmpleadoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Empleado
    fields = ('__all__')
    template_name = 'empleados/crear_empleado.html'
    success_url = reverse_lazy('lista-empleados')
    success_message = 'Empleado creado exitosamente.'

class EmpleadoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Empleado
    fields = ('__all__')
    template_name = 'empleados/actualizar_empleado.html'
    success_url = reverse_lazy('lista-empleados')
    success_message = 'Empleado actualizado exitosamente.'

class EmpleadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Empleado
    template_name = 'empleados/eliminar_empleado.html'
    success_url = reverse_lazy('lista-empleados')