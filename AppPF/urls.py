from django.urls import path
from AppPF import views
#una path para cada Templeate, menos base que es el padre
urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('Empleados/', views.empleados, name="Empleados"),
    path('Productos/', views.productos, name="Productos"),
    path('Clientes/', views.clientes, name="Clientes"),
    path('buscar/', views.buscar),
    ]