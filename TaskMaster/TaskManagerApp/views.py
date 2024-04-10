from django.shortcuts import render
from django.http import HttpResponse

def homeview(request):
    return HttpResponse("¡Hola, mundo! Esta es la página de inicio de la aplicación.")

def list_view():
    pass

"""def index(request):
    # Lógica para la página de inicio
    return render(request, 'TaskManagerApp/index.html')

def tareas(request):
    # Obtener todas las tareas
    tareas = Tarea.objects.all()
    return render(request, 'TaskManagerApp/tareas.html', {'tareas': tareas})

def detalle_tarea(request, tarea_id):
    # Obtener los detalles de una tarea específica
    tarea = Tarea.objects.get(pk=tarea_id)
    return render(request, 'TaskManagerApp/detalle_tarea.html', {'tarea': tarea})"""
