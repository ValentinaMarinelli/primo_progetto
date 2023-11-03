from django.shortcuts import render
import random

# Create your views here.

def index_prova1(request):
    return render(request, "index_prova1.html")

def maxmin(request):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    somma = num1+num2
    context = {
        'num1' : num1,
        'num2' : num2,
        'somma' : somma,
    }
    return render(request, "maxmin.html", context)

def media(request):
    numeri = []
    i = 1
    somma = 0
    for i in range(30):
        numeri.append(random.randint(1,10))
        somma+=numeri[i]
    media = (somma/30)
    context = {
        'numeri' : [],
        'i' : i,
        'somma' : somma,
        'media' : media,
    }
    return render(request, "media.html", context)

def voti(request):
    context = {
        'tabella' : {
            'Paolo Rossi':6,
            'Matteo Ferrari':9,
            'Luca Verdi':4,
        },
    }
    return render(request, "voti.html",context)



