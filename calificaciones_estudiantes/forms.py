from django import forms
from .models import Calificacion

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        exclude = ['promedio']
        widgets = {
            'nombre_estudiante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'identificacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de identificación'}),
            'asignatura': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la asignatura'}),
            'nota1': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '5'}),
            'nota2': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '5'}),
            'nota3': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '5'}),
        }
        labels = {
            'nombre_estudiante': 'Nombre del Estudiante',
            'identificacion': 'Identificación',
            'asignatura': 'Asignatura',
            'nota1': 'Nota 1',
            'nota2': 'Nota 2',
            'nota3': 'Nota 3',
        }
