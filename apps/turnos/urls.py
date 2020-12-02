
from django.conf.urls import url
from .views import turnoList, verTurnoEsp, turnoCreation, turnoUpdate, turnoDelete
from django.urls import path, include
from .views import Render_html
app_name='turnos'
urlpatterns = [
    path("turnos-list", turnoList.as_view(), name="listar"),
    path("turnos-create", turnoCreation.as_view(), name="cargar"),
    path("ver-turno/<pk>", verTurnoEsp.as_view(), name="ver"),
    path("editar-turno/<pk>", turnoUpdate.as_view(), name="modificar"),
    path("borrar-turno/<pk>", turnoDelete.as_view(), name="borrar"),
    path('RenderHTML', Render_html, name='render')
]

