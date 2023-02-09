from django.shortcuts import render
from .models import peliculas

#vista basada en funcion que me permite renderizar
#a mi template(html)
def index(request):
    template_name="index.html"
    #select * from peliculas
    pls=peliculas.objects.all()
    context = {
        "peliculas":pls
    }
    return render(request,template_name,context)

def buscar(request):
    template_name="index.html"
    if request.method=="GET":
        #Guardando en una variable el valos del input
        query=request.GET.get('q')
        #filtrando de la tabla peliculas de acuerdo a la variable
        results = peliculas.objects.filter(reseña__icontains=query)
        #creando un contexto con el resultado del filtro
        context = {
            "peliculas":results
        }
        #renderizando en el template
    return render(request,template_name,context)    


def detalles(request,id_pelicula=None):
    template_name="detalles.html"
    #select * from peliculas where id=?
    pel = peliculas.objects.get(pk=id_pelicula)
    context = {
        "pelicula":pel
    }
    return render(request,template_name,context)






