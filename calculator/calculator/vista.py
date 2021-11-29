from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from calculator.calculo import *

def index(request):
    data= request.POST.get("input_solved")
    resultado = data
    resultado = sumar(resultado)
    print(type(resultado))
    return render (request, 'index.html',{'data':resultado})

def buscar(request):
    # mensaje= "llego el calculo %r" %request.GET["input_solved"]
    pass
    # return HttpResponse(mensaje)