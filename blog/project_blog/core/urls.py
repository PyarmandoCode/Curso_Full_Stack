from django.urls import path

from .views import index

urlpatterns = [
    #todo esta ruta de la aplicacio core es la que se levantara por default
    path('', index),
]
