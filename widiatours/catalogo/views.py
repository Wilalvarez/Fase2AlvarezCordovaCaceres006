from django.shortcuts import render
from .models import Compra
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic

class CompraCreate(CreateView):
    model = Compra
    fields = '__all__'


class CompraUpdate(UpdateView):
    model = Compra
    fields = ['name','precio','descripcion']
    
class CompraDelete(DeleteView):
    model = Compra
    success_url = reverse_lazy('tienda.html')


class CompraDetailView(generic.DetailView):
    model = Compra

class CompraListView(generic.ListView):
    model = Compra

#LOGIN 
def iniciosesion(request):

    return render(
        request,
        'iniciosesion.html',
    )

def creacionusuario(request):

    return render(
        request,
        'creacionusuario.html',
    )


#PAGINAS
def index(request):
    num_compras=Compra.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_compras':num_compras},
    )

def acercadeee(request):

    return render(
        request,
        'acercadeee.html',
    )

def tienda(request):

    return render(
        request,
        'tienda.html',
    )

def quehacer(request):

    return render(
        request,
        'quehacer.html',
    )

#----------TIENDA -------------

#ACCESORIOS
def camping(request):

    return render(
        request,
        'camping.html',
    )

def playa(request):

    return render(
        request,
        'playa.html',
    )

def nieve(request):

    return render(
        request,
        'nieve.html',
    )

def kayak(request):

    return render(
        request,
        'kayak.html',
    )


def trekking(request):

    return render(
        request,
        'trekking.html',
    )

def ciclismo(request):

    return render(
        request,
        'ciclismo.html',
    )

#VESTIMENTA

def chaqueta(request):

    return render(
        request,
        'chaqueta.html',
    )

def poleron(request):

    return render(
        request,
        'poleron.html',
    )

def polera(request):

    return render(
        request,
        'polera.html',
    )

def pantalon(request):

    return render(
        request,
        'pantalon.html',
    )

def short(request):

    return render(
        request,
        'short.html',
    )

def calzado(request):

    return render(
        request,
        'calzado.html',
    )

