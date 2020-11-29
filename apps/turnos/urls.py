
from django.conf.urls import url
from .views import turnoList, verTurnoEsp, turnoCreation, turnoUpdate, turnoDelete
from django.urls import path, include
from .views import Render_html
app_name='turnos'
urlpatterns = [
    path("turnos-list", turnoList.as_view(), name="listar"),
    path("turnos-create", turnoCreation.as_view(), name="crear"),
    path("ver-turno", verTurnoEsp.as_view(), name="ver"),
    path("editar-turno", turnoUpdate.as_view(), name="editar"),
    path("borrar-turno", turnoDelete.as_view(), name="borrar"),
    path('RenderHTML', Render_html, name='render')
]

