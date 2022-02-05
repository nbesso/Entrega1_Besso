from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def otro_saludo(request):
    return HttpResponse("<h1>Hola!</h1></br><p>Esta es mi segunda vista</p>")