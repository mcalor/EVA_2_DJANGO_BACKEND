from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Tarea
from .forms import TareaForm


# ---------------------------
# LISTA DE TAREAS
# ---------------------------
class TareaLista(ListView):
    model = Tarea
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get("q")
        vigente = self.request.GET.get("vigente")
        vencidas = self.request.GET.get("vencidas")

        qs = Tarea.objects.all()

        # búsqueda en título o descripción
        if q:
            qs = qs.filter(Q(titulo__icontains=q) | Q(descripcion__icontains=q))

        # filtrar por vigencia (vigente=True/False)
        if vigente in ("true", "false"):
            qs = qs.filter(vigente=(vigente == "true"))

        # filtrar por tareas vencidas (fecha_limite < hoy)
        if vencidas == "1":
            hoy = self.request.today
            qs = qs.filter(fecha_limite__lt=hoy)

        return qs.order_by("-fecha_creacion")

    # ayuda para usar 'hoy' en los filtros sin importar tz
    def dispatch(self, request, *args, **kwargs):
        self.request.today = timezone.localdate()
        return super().dispatch(request, *args, **kwargs)


# ---------------------------
# DETALLE DE TAREA
# ---------------------------
class TareaDetalle(DetailView):
    model = Tarea

    def get_queryset(self):
        # Podrías prefetch/annotate si tuvieras relaciones
        return Tarea.objects.all()


# ---------------------------
# CREAR TAREA
# ---------------------------
class TareaCrear(CreateView):
    model = Tarea
    form_class = TareaForm
    success_url = reverse_lazy("tareas:tarea_list")


# ---------------------------
# EDITAR TAREA
# ---------------------------
class TareaEditar(UpdateView):
    model = Tarea
    form_class = TareaForm
    success_url = reverse_lazy("tareas:tarea_list")


# ---------------------------
# ELIMINAR TAREA
# ---------------------------
class TareaEliminar(DeleteView):
    model = Tarea
    success_url = reverse_lazy("tareas:tarea_list")
