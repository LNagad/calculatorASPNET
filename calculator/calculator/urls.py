
from django.contrib import admin
from django.urls import path
from calculator.vista import buscar,index


# estructura: from proyecto.vista import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('buscar/', buscar)
]
