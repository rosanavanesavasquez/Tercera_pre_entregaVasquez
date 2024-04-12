from django.shortcuts import render
from django.http import HttpResponse
from TaskManagerApp.models import Tarea

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
