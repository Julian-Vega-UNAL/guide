from django.contrib import admin
from Computadoras.models import Procesador, Empresa, Computadoras
# Register your models here.
admin.site.register(Computadoras)
admin.site.register(Empresa)
admin.site.register(Procesador)

