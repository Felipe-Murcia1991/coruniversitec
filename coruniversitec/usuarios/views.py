from django.http import HttpResponse



# Create your views here.
#primera impresion con funcion

def Bienvenidos(request):
    return HttpResponse("Bienvenidos a SDAF")
