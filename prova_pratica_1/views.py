from django.shortcuts import render
import datetime
import random
# Create your views here.

def somma(request):

    var = {'var1' : random.randint(0-10), 'var2' : random.randint(0-10)}
    somma = var1 + var2
    dic = { 'var1' : var1, 'var2' : var2, 'somma' : somma}
    return render(request, "prova_pratica_1/somma.html", dic)

def media(request):

    lista = []
    somma = 0

    for _ in range (30):
        lista.append(random.randint(1,10))
        for i in range(30):
            somma += lista[i]
    media = somma / 30

    dic = {'media' : media}
    return render(request, "prova_pratica_1/media.html", dic)


def voti(request):

    return render(request, "voti.html", dic)
