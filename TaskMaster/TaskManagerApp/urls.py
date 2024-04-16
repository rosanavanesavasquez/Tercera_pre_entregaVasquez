from django.urls import path
from .views import homeview, list_view, index, tareas, detalle_tarea, crear_tarea, crear_categoria

urlpatterns = [
    path('', homeview, name='home'),  # Página de inicio
    path('list/', list_view, name='list'),  # Página de lista de tareas
    path('index/', index, name='index'),  # Página de índice
    path('tareas/', tareas, name='tareas'),  # Página de todas las tareas
    path('detalle_tarea/<int:tarea_id>/', detalle_tarea, name='detalle_tarea'),  # Detalle de tarea
    path('crear_tarea/', crear_tarea, name='crear_tarea'),  # Vista para crear una nueva tarea
    path('crear-categoria/', crear_categoria, name='crear_categoria')
]