from django import forms
from empleadoApp.models import Empleado

class EmpleadoRegistroForm(forms.Form):
    nombre = forms.CharField()
    email = forms.CharField()
    telefono = forms.CharField()

class EmpleadoRegistroForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'