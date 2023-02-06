
from django.contrib import admin
from django.urls import path,include

#app_name=""
urlpatterns = [
    path('admin/', admin.site.urls),
    #esto se ejecuta por primera vez
    path('',include('core.urls'))

]
