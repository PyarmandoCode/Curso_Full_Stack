from django.urls import path
from .views import index,clientes

app_name="core"

urlpatterns = [
    path('index',index),
    path('clientes',clientes),
]
