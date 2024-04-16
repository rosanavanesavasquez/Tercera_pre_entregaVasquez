from django.shortcuts import render, redirect
from django.http import HttpResponse
from TaskManagerApp.models import Tarea
from .forms import TareaForm, CategoriaForm

def homeview(request):
    return render(request, "TaskManagerApp/home.html")

def list_view():
    pass

def index(request):
    # Obtener las tareas pendientes
    tareas_pendientes = Tarea.objects.filter(completada=False)
    return render(request, 'TaskManagerApp/index.html', {'tareas': tareas_pendientes})

def tareas(request):
    # Obtener todas las tareas
    tareas = Tarea.objects.all()
    return render(request, 'TaskManagerApp/tareas.html', {'tareas': tareas})

def detalle_tarea(request, tarea_id):
    # Obtener los detalles de una tarea específica
    tarea = Tarea.objects.get(pk=tarea_id)
    return render(request, 'TaskManagerApp/detalle_tarea.html', {'tarea': tarea})

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            # Asegurarse de que la fecha está en el formato correcto antes de guardarla
            tarea.fecha_limite = form.cleaned_data['fecha_limite']
            tarea.usuario = request.user  # Asigna el usuario actual al campo usuario
            tarea.save()
            return redirect('tareas')  # Redirigir a la página de tareas después de crear la tarea
    else:
        form = TareaForm()
    return render(request, 'TaskManagerApp/crear_tarea.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Puedes redirigir a cualquier página después de crear la categoría
    else:
        form = CategoriaForm()
    return render(request, 'TaskManagerApp/crear_categoria.html', {'form': form})
