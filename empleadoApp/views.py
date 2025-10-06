from django.shortcuts import render
from empleadoApp.models import Empleado
from empleadoApp.forms import EmpleadoRegistroForm

#Libreiras para redireccionar
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def empleadoData(request):
    # SELECT * FROM
    empleados = Empleado.objects.all()
    data = {'empleados' : empleados}
    return render(request, 'empleadoApp/empleados.html', data)

def crearEmpleado(request):
    form = EmpleadoRegistroForm()

    if request.method == 'POST':
        form = EmpleadoRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('empleadoData'))

    data = {'form' : form}
    return render(request, 'empleadoApp/empleadoRegistro.html', data)
