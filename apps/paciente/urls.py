from django.urls import path
from .views import Listar


app_name='paciente'
urlpatterns = [
    path("listar", Listar.as_view(), name="listar"),
    
]