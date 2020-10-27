from django.shortcuts import render
from .models import Compra


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

