from django.shortcuts import render

# Create your views here.

voti = {'Giuseppe Gullo':[("Matematica",9,0), ("Italiano",7,3), ("Inglese",7,4), ("Storia",7,4), ("Geografia",5,7)],
            'Antonio Barbera':[("Matematica",8,1), ("Italiano",6,1), ("Inglese",9,0), ("Storia",8,2), ("Geografia",8,1)],
            'Nicola Spina':[("Matematica",7,2), ("Italiano",6,2), ("Inglese",4,3), ("Storia",8,2), ("Geografia",8,2)]}

def index_voti(request):
    return render(request, "index_voti.html")

def view_a(request):
    materie = ["Matematica", "Italiano", "Inglese", "Storia", "Geografia"]
    context = {
        'materie' : materie,
    }
    print(context)
    return render(request, "lista_materie.html", context)

def view_b(request):
    i = 0
    for studente,dati in voti.items():
        print(studente)
        for i in range(4):
            print(voti[studente][i])
    
    context = {
        'voti' : voti,
        'i' : i,
        'studente' : studente,
        'dati' : dati,
    }
    print(context)
    return render(request, "voti_studenti.html", context)

def view_c(request):
    i = 0
    for studente in voti.keys():
        somma = 0
        media = 0
        for i in range(4):
            somma+=voti[studente][i][1]
        media = somma/5
        print(media)
        
    context = {
        'somma' : somma,
        'media' : media,
        'studente' : studente,
        'voti' : voti,
        'i' : i,
        }
    print(context)
    return render(request, "media_studenti.html", context)

def view_d(request):
    voto_massimo = 0
    materie_voto_massimo = ""
    studenti_voto_massimo = ""
    voto_minimo = 0
    matere_voto_minimo = ""
    studenti_voto_minimo = ""
    context = {
        'voto_massimo' : voto_massimo,
        'materie_voto_massimo' : materie_voto_massimo,
        'studenti_voto_massimo' : studenti_voto_massimo,
        'voto_minimo' : voto_minimo,
        'matere_voto_minimo' : matere_voto_minimo,
        'studenti_voto_minimo' : studenti_voto_minimo,
    }
    print(context)
    return render(request, "max_min_voti.html", context)

    

