#Va lo de Modelo
from django import forms

class ProductosFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    cantidad = forms.IntegerField()


class EmpleadosFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)


class ClientesFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    telefono = forms.IntegerField()