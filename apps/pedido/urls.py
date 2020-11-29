from django.urls import path
from .views import Render_html


app_name='pedido'
urlpatterns = [
    path('RenderHTML', Render_html, name='render')
]