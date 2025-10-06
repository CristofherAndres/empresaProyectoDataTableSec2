from django import forms
from empleadoApp.models import Empleado

#Importar libreria para validaciones
from django.core import validators

#Sirve para editar
class EmpleadoRegistroForm(forms.Form):
    #  El nombre no puede tener menos de 5 caracteres y no mas de 10
    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(5),
        validators.MaxLengthValidator(10)
    ])
    email = forms.CharField()
    telefono = forms.CharField()

    def clean_email(self):
        inputEmail = self.cleaned_data['email']
        if inputEmail.find('@') == -1:
            raise forms.ValidationError("El correo debe tener un @")
        return inputEmail

    nombre.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'

    nombre.label = "Nombre empleado"
    email.label = "Correo electronico"

#Sirve para insertar
class EmpleadoRegistroForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

    #  El nombre no puede tener menos de 5 caracteres y no mas de 10
    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(5),
        validators.MaxLengthValidator(10)
    ])
    email = forms.CharField()
    telefono = forms.CharField()

    def clean_email(self):
        inputEmail = self.cleaned_data['email']
        if inputEmail.find('@') == -1:
            raise forms.ValidationError("El correo debe tener un @")
        return inputEmail

    nombre.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'

    nombre.label = "Nombre empleado"
    email.label = "Correo electronico"