from django.shortcuts import render

from .models import post


def index(request):
    template_name = "index.html"
    # todo select * from core_post
    # todo ORM - Recuperame todos los registros de la tabala post
    posts_data = post.objects.all()
    #todo creo un archivo de contexto (JSON) todo le paso la informacion de la variable POSTS
    context = {
        "posts": posts_data
    }

    return render(request, template_name, context)
