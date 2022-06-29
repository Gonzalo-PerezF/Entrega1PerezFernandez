from itertools import product
from django.shortcuts import render, HttpResponse
from AppPF.models import *
from AppPF.forms import *

# Create your views here.
def inicio(request):

    return render(request, "AppPF/inicio.html")



def empleados(request):

    if request.method == 'POST':

        miFormulario = EmpleadosFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            info = miFormulario.cleaned_data
            print(info)

            empleado = Empleados(nombre=info['nombre'], apellido=info['apellido'])
            empleado.save()

            return render(request, "AppPF/inicio.html")
    else:
        miFormulario = EmpleadosFormulario()

    return render(request, "AppPF/empleados.html", {"miFormulario":miFormulario})

def productos(request):

    if request.method == 'POST':

        miFormulario = ProductosFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            info = miFormulario.cleaned_data
            print(info)

            producto = Productos(nombre=info['nombre'], cantidad=info['cantidad'])
            producto.save()

            return render(request, "AppPF/inicio.html")
    else:
        miFormulario = EmpleadosFormulario()

    return render(request, "AppPF/empleados.html", {"miFormulario":miFormulario})



def clientes(request):

    if request.method == 'POST':

        miFormulario = ClientesFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            info = miFormulario.cleaned_data
            print(info)

            clientes = Clientes(nombre=info['nombre'],apellido=info['apellido'], telefono=info['telefono'])
            clientes.save()

            return render(request, "AppPF/inicio.html")
    else:
        miFormulario = ClientesFormulario()

    return render(request, "AppPF/clientes.html", {"miFormulario":miFormulario})


def buscar(request):

    if request.GET['productos']:

        productos = request.GET['productos']
        print(productos)
    
        productos = Productos.objects.filter(productos__icontains=productos)
        print(productos)

        return render(request, "AppPF/inicio.html", {"productos":productos.values,"prd":productos})
    else:

        respuesta = "Sin datos"

    return render(request, "AppPF/inicio.html", {"prd":respuesta})
