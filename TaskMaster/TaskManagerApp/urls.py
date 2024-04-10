from django.urls import path
from .views import homeview, list_view

urlpatterns = [
    path('', homeview, name='home'),  # URL raíz
    path("list/", list_view),
]