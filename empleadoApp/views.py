from django.shortcuts import render
from empleadoApp.models import Empleado

# Create your views here.
def empleadoData(request):
    # SELECT * FROM
    empleados = Empleado.objects.all()
    data = {'empleados' : empleados}
    return render(request, 'empleadoApp/empleados.html', data)
