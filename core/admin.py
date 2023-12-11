from django.contrib import admin
from .models import Usuario, Vehiculo, tipoUsuario, Viaje, Sede

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Vehiculo)
admin.site.register(tipoUsuario)
admin.site.register(Viaje)
admin.site.register(Sede)
