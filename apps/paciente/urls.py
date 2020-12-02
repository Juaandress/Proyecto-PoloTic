from django.urls import path
from .views import Listar,ModHistorial,Ver,VerHistorial


app_name='paciente'
urlpatterns = [
    path("listar", Listar.as_view(), name="listar"),
    path("ver/<pk>", Ver.as_view(), name="ver"),
    path("historial/<pk>", VerHistorial.as_view(), name="historial"),
    path("modhistorial/<pk>", ModHistorial.as_view(), name="modhistorial"),
]