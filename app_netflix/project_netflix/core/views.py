from django.shortcuts import render
from .models import peliculas

#vista basada en funcion que me permite renderizar
#a mi template(html)
def index(request):
    template_name="index.html"
    pls=peliculas.objects.all()
    context = {
        "peliculas":pls
    }
    return render(request,template_name,context)


