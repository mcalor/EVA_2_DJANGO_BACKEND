from django import forms
from .models import Tarea


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = [
            "titulo",
            "descripcion",
            "prioridad",
            "vigente",
            "fecha_creacion",
            "fecha_limite",
        ]
