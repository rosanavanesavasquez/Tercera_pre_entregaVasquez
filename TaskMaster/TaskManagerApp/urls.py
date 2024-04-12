from django.urls import path
from .views import homeview, list_view, index, tareas, detalle_tarea

urlpatterns = [
    path('', homeview, name='home'),  # Página de inicio
    path('list/', list_view, name='list'),  # Página de lista de tareas
    path('index/', index, name='index'),  # Página de índice
    path('tareas/', tareas, name='tareas'),  # Página de todas las tareas
    path('detalle_tarea/<int:tarea_id>/', detalle_tarea, name='detalle_tarea'),  # Detalle de tarea
]