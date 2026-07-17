from django.contrib import admin
from .models import Contacto


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "correo", "telefono")
    search_fields = ("nombre", "correo", "telefono")
