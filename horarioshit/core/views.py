from django.shortcuts import render
from .models import Ramos

# Create your views here.

def home(request):
    ramo = Ramos.objects.all()
    return render(request, "core/home.html", {'ramo':ramo})

def otramierda(request):
    ramo2 = Ramos.objects.filter(horario = 'A')
    return  render(request, 'core/shit.html', {"ramo2": ramo2})