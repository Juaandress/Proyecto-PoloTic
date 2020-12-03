from django.urls import path
from .views import Render_html, asistencia_turnos,paciente_pedido,productos_mas_vendidos,ventas_totales_por_mes,no_asistencia_turnos



app_name='reporte'
urlpatterns = [
    path('RenderHTML', Render_html, name='render'),
    path('asistencia', asistencia_turnos, name='asistencia'),
    path('no_asistencia', no_asistencia_turnos, name='no_asistencia'),
    path('paciente_pedido', paciente_pedido, name='paciente_pedido'),
    path('pmv', productos_mas_vendidos, name='pmv'),
    path('vt', ventas_totales_por_mes, name='vt'),
]