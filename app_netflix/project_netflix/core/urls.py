from django.urls import path

from .views import index,buscar,detalles,crear

app_name="core"

urlpatterns = [
    path('', index,name="inicio"),
    path('buscar/', buscar,name="search"),
    path('detalles/<int:id_pelicula>', detalles,name="detail"),
    path('crear/', crear,name="create"),
]