from django.shortcuts import render

def Render_html(request):
    return render(request,'Pedidos/pedidos.html')