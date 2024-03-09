from django.shortcuts import render, redirect
from .models import Alumno
from .forms import AlumnoForm

def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos/listar_alumnos.html', {'alumnos': alumnos})

def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'alumnos/agregar_alumno.html', {'form': form})

def calcular_estadisticas(alumnos):
    edades = [alumno.calcular_edad() for alumno in alumnos]
    promedio_edad = sum(edades) / len(edades) if len(edades) > 0 else 0
    return {'edades': edades, 'promedio_edad': promedio_edad}
