from django.contrib import admin
from empleadoApp.models import Empleado

# Register your models here.
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','email']
    
    
# Register your models here.
admin.site.register(Empleado, EmpleadoAdmin)
