from django.urls import path
from . import views

app_name = "contactos"

urlpatterns = [
    path("", views.index, name="index"),
    path("api/contactos/", views.contacto_list, name="contacto_list"),
    path("api/contactos/crear/", views.contacto_create, name="contacto_create"),
    path("api/contactos/<int:pk>/editar/", views.contacto_update, name="contacto_update"),
    path("api/contactos/<int:pk>/eliminar/", views.contacto_delete, name="contacto_delete"),
]
