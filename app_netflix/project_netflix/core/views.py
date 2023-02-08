from django.shortcuts import render

#vista basada en funcion que me permite renderizar
#a mi template(html)
def index(request):
    template_name="index.html"
    return render(request,template_name)


