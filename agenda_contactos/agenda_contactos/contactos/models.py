from django.db import models


class Contacto(models.Model):
    

    nombre = models.CharField(max_length=150, verbose_name="Nombre completo")
    correo = models.EmailField(max_length=254, verbose_name="Correo electrónico")
    telefono = models.CharField(max_length=20, verbose_name="Número telefónico")

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return self.nombre

    def to_dict(self):
        
        return {
            "id": self.id,
            "nombre": self.nombre,
            "correo": self.correo,
            "telefono": self.telefono,
        }
