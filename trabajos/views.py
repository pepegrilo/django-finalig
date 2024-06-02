# trabajos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import TrabajoDeGrado, Modalidad, Actividad, Estudiante, Profesor, Programa, Jurado, Empresa, Estado, Evaluacion
from .forms import TrabajoDeGradoForm

def index(request):
    trabajos = TrabajoDeGrado.objects.all()
    return render(request, 'trabajos/index.html', {'trabajos': trabajos})

def detalle_trabajo(request, trabajo_id):
    trabajo = get_object_or_404(TrabajoDeGrado, pk=trabajo_id)
    return render(request, 'trabajos/detalle.html', {'trabajo': trabajo})


def crear_trabajo(request, pk=None):
    if pk:
        trabajo = get_object_or_404(TrabajoDeGrado, pk=pk)
    else:
        trabajo = TrabajoDeGrado()

    if request.method == 'POST':
        form = TrabajoDeGradoForm(request.POST, instance=trabajo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TrabajoDeGradoForm(instance=trabajo)

    return render(request, 'trabajos/crear.html', {'form': form})

def obtener_actividades(request):
    modalidad_id = request.GET.get('modalidad_id')
    if modalidad_id:
        actividades = list(Actividad.objects.filter(modalidad_id=modalidad_id).values('id', 'nombre'))
    else:
        actividades = []
    return JsonResponse(actividades, safe=False)