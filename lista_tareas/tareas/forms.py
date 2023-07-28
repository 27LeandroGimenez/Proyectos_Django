from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'completado']
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su nombre'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Ingrese alguna descripcion...'}),
            'completado':forms.CheckboxInput(attrs={"class":"form-check-input mb-5", "style":'text-align: start;'}),
        }
        labels = {
            'nombre':'', 'descripcion':'', 'completado':'Completada',
        }