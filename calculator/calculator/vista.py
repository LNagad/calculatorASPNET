from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render (request, 'index.html')

def buscar(request):
    mensaje= "llego el calculo %r" %request.GET["input_solved"]

    return HttpResponse(mensaje)