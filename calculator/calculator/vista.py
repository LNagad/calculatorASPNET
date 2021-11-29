from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from calculator.calculo import *

def index(request):
    data= request.POST.get("input_solved")
    if data == None:
        data = ''
    data = bobito(data)
    # print(data)
    # print(type(data))
    return render (request, 'index.html',{'data':data})

def buscar(request):
    # mensaje= "llego el calculo %r" %request.GET["input_solved"]
    pass
    # return HttpResponse(mensaje)