from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import Contacto
from .forms import ContactoForm


def index(request):

    return render(request, "contactos/index.html")


@require_http_methods(["GET"])
def contacto_list(request):
    
    query = request.GET.get("q", "").strip()
    contactos = Contacto.objects.all()
    if query:
        contactos = contactos.filter(nombre__icontains=query)
    data = [c.to_dict() for c in contactos]
    return JsonResponse({"ok": True, "contactos": data})


@require_http_methods(["POST"])
def contacto_create(request):
   
    form = ContactoForm(request.POST)
    if form.is_valid():
        contacto = form.save()
        return JsonResponse({"ok": True, "contacto": contacto.to_dict()}, status=201)
    return JsonResponse({"ok": False, "errors": form.errors}, status=400)


@require_http_methods(["POST"])
def contacto_update(request, pk):

    contacto = get_object_or_404(Contacto, pk=pk)
    form = ContactoForm(request.POST, instance=contacto)
    if form.is_valid():
        contacto = form.save()
        return JsonResponse({"ok": True, "contacto": contacto.to_dict()})
    return JsonResponse({"ok": False, "errors": form.errors}, status=400)


@require_http_methods(["POST"])
def contacto_delete(request, pk):
   
    contacto = get_object_or_404(Contacto, pk=pk)
    contacto.delete()
    return JsonResponse({"ok": True})
