from django.contrib import admin
from .models import Tarea


@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "prioridad",
        "vigente",
        "fecha_creacion",
        "fecha_limite",
    )
    list_filter = ("vigente", "prioridad", "fecha_limite")
    search_fields = ("titulo", "descripcion")
    actions = ["marcar_no_vigentes"]

    @admin.action(description="Marcar seleccionadas como NO vigentes")
    def marcar_no_vigentes(self, request, queryset):
        updated = queryset.update(vigente=False)
        self.message_user(request, f"{updated} tareas marcadas como no vigentes.")
