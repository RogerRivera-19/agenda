import re
from django import forms
from .models import Contacto

# Un teléfono válido puede incluir dígitos, espacios, guiones y un signo "+"
# al inicio, pero nunca letras.
PATRON_TELEFONO = re.compile(r"^[0-9+\-\s()]+$")


class ContactoForm(forms.ModelForm):
    """Formulario de creación/edición de contactos con validaciones de negocio."""

    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "telefono"]
        error_messages = {
            "correo": {
                "invalid": "Ingresa un correo electrónico con un formato válido (ej. nombre@dominio.com).",
            },
        }

    def clean_nombre(self):
        nombre = (self.cleaned_data.get("nombre") or "").strip()
        if not nombre:
            raise forms.ValidationError("El nombre es obligatorio.")
        return nombre

    def clean_correo(self):
        correo = (self.cleaned_data.get("correo") or "").strip()
        if not correo:
            raise forms.ValidationError("El correo electrónico es obligatorio.")
        return correo

    def clean_telefono(self):
        telefono = (self.cleaned_data.get("telefono") or "").strip()
        if not telefono:
            raise forms.ValidationError("El teléfono es obligatorio.")
        if not PATRON_TELEFONO.match(telefono):
            raise forms.ValidationError(
                "El teléfono solo puede contener números (y opcionalmente +, - o espacios)."
            )
        if not re.search(r"\d", telefono):
            raise forms.ValidationError("El teléfono debe contener al menos un número.")
        return telefono
