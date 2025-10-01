from django.urls import path
from . import views


app_name = "tareas"


urlpatterns = [
    path("", views.TareaLista.as_view(), name="tarea_list"),
    path("tarea/<int:pk>/", views.TareaDetalle.as_view(), name="tarea_detail"),
    path("tarea/nueva/", views.TareaCrear.as_view(), name="tarea_create"),
    path("tarea/<int:pk>/editar/", views.TareaEditar.as_view(), name="tarea_update"),
    path("tarea/<int:pk>/eliminar/", views.TareaEliminar.as_view(), name="tarea_delete"),
]

