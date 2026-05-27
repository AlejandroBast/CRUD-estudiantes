from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Avg
from .models import Calificacion
from .forms import CalificacionForm

def listar(request):
    calificaciones = Calificacion.objects.all()
    promedio_general = Calificacion.objects.aggregate(Avg('promedio'))['promedio__avg']
    return render(request, 'calificaciones/listar.html', {
        'calificaciones': calificaciones,
        'promedio_general': round(promedio_general, 2) if promedio_general else None
    })

def crear(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Calificación registrada correctamente.')
            return redirect('listar')
    else:
        form = CalificacionForm()
    return render(request, 'calificaciones/crear.html', {'form': form})

def editar(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Calificación actualizada correctamente.')
            return redirect('listar')
    else:
        form = CalificacionForm(instance=calificacion)
    return render(request, 'calificaciones/editar.html', {'form': form, 'calificacion': calificacion})

def eliminar(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        calificacion.delete()
        messages.success(request, 'Calificación eliminada correctamente.')
        return redirect('listar')
    return render(request, 'calificaciones/eliminar.html', {'calificacion': calificacion})

def promedio_general(request):
    promedio = Calificacion.objects.aggregate(Avg('promedio'))['promedio__avg']
    total = Calificacion.objects.count()
    return render(request, 'calificaciones/promedio_general.html', {
        'promedio_general': round(promedio, 2) if promedio else None,
        'total_estudiantes': total
    })
