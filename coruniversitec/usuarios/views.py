from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCerationsForm
from django.views.generic import CreateView
from djanfo.core.urlresolvers import reverse_lazy


# Create your views here.
#primera impresion con funcion

def Bienvenidos(request):
    return HttpResponse("Bienvenidos a SDAF")


class RegistroUsuario(CreateView):
    model=UserCerationsForm
    template_name="usuarios/registro.html"
    form_class=UserCerationsForm
    success_url=reverse_lazy
