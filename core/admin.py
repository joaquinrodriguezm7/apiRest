from django.contrib import admin
from .models import Usuario, Vehiculo, tipoUsuario, Viaje

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Vehiculo)
admin.site.register(tipoUsuario)
admin.site.register(Viaje)
