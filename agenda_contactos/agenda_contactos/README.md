# Agenda de Contactos (Django)

Aplicación web para gestionar los contactos de los empleados de una empresa:
registrar, listar, buscar en tiempo real, editar y eliminar contactos.

## Requisitos
- Python 3.10+
- pip

## Instalación y ejecución

```bash
# 1. Crear y activar un entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate        # En Windows: venv\Scripts\activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Aplicar migraciones (crea la base de datos SQLite)
python manage.py migrate

# 4. (Opcional) Crear un superusuario para acceder al panel /admin
python manage.py createsuperuser

# 5. Levantar el servidor de desarrollo
python manage.py runserver
```

Luego abre tu navegador en **http://127.0.0.1:8000/**

## Estructura del proyecto

```
agenda_contactos/
├── manage.py
├── requirements.txt
├── agenda_contactos/        # Configuración del proyecto (settings, urls)
└── contactos/                # App principal
    ├── models.py             # Modelo Contacto (nombre, correo, telefono)
    ├── forms.py               # ContactoForm con validaciones de negocio
    ├── views.py                # Vistas: index + API JSON (listar/crear/editar/eliminar)
    ├── urls.py
    ├── admin.py
    └── templates/contactos/index.html   # Formulario + lista + buscador (HTML/CSS/JS)
```

## Funcionalidades implementadas

1. **Registrar contactos**: formulario con Nombre, Correo y Teléfono. Botón "Guardar".
2. **Listar contactos**: se muestran inmediatamente debajo del formulario, con botones
   Editar y Eliminar en cada tarjeta.
3. **Búsqueda en tiempo real**: la caja de búsqueda filtra la lista por nombre mientras
   se escribe (sin botón "Buscar"), usando `fetch` hacia `/api/contactos/?q=...`.
4. **Editar contacto**: al presionar "Editar" se cargan los datos en el formulario, el
   botón cambia a "Actualizar" y al guardar se modifica únicamente ese registro (no se
   crea uno nuevo).
5. **Eliminar contacto**: pide confirmación (`confirm()`) y luego elimina el contacto,
   actualizando la lista de inmediato.

## Validaciones

Tanto en el cliente (JavaScript, para una respuesta inmediata) como en el servidor
(Django Forms, como fuente de verdad) se valida que:

- Ningún campo esté vacío.
- El correo tenga un formato válido (`usuario@dominio.com`).
- El teléfono no contenga letras (solo números, espacios, `+`, `-` y paréntesis).

Los mensajes de error se muestran debajo de cada campo del formulario.

## Notas técnicas

- El backend expone una pequeña API JSON (`/api/contactos/...`) consumida por
  JavaScript "vanilla" (sin frameworks externos), cumpliendo con búsqueda en tiempo
  real sin recargar la página.
- Cada contacto se representa como un objeto `{id, nombre, correo, telefono}`, tal
  como se pidió en el enunciado.
- Puedes administrar los contactos también desde `/admin/` (tras crear un
  superusuario).
