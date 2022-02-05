from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def otro_saludo(request):
    return HttpResponse("<h1>Hola!</h1></br><p>Esta es mi segunda vista</p>")

def template1(request):
    return render(request, "template1.html")

def template2(request):
    context = {"curso": "Python"}
    return render(request, "template2.html", context)

def template3(request, nombre):
    context = {"nombre": nombre}
    return render(request, "template3.html", context)

def template4(request):
    context = {"lista": [1,2,3,4,5]}
    return render(request, "template4.html", context) 