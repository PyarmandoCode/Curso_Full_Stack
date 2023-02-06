from django.shortcuts import render


#todo esta es una vista basada en funcion
def index(request):
    #la Plantilla que voy a mostrar el el navegador
    template_name="index.html"
    #renderizarlos en el navegador
    return render(request,template_name)


#todo esta es una vista basada en funcion
def clientes(request):
    #la Plantilla que voy a mostrar el el navegador
    template_name="clientes.html"
    #renderizarlos en el navegador
    return render(request,template_name)
