from django.shortcuts import render, get_object_or_404
from .models import Articolo, Giornalista

# Create your views here.

def home(request):
    """a = ""
    g = ""
    for art in Articolo.objects.all():
        a += (art.titolo + "<br>")

    for gio in Giornalista.objects.all():
        g += (gio.nome + "<br>")
    response = "Articoli:<br>" + a + "<br>Giornalisti:<br>" + g

    return HttpResponse("<h1>" + response + "</h1>")""" 
    #Nella nuova versione seguente "a" e "g" sono due array, mentre precedentemente erano due stringhe
    """a = []
    g = []
    for art in Articolo.objects.all():
        a.append(art.titolo)

    for gio in Giornalista.objects.all():
        g.append(gio.nome)

    response = str(a) + "<br>" + str(g)
    print(response)

    return HttpResponse("<h1>" + response + "</h1>")"""
    #Nella nuova versione le variabili "articoli" e "giornalisti" contengono le istanze delle rispettive classi
    #Vengono unite nella variabile "context" e successivamente stampate e passate alla pagina "homepage.html"
    articoli = Articolo.objects.all()  
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "homepage_news.html", context)

def articoloDetailView(request, pk):
    # articolo = Articolo.objects.get(pk=pk)
    articolo = get_object_or_404(Articolo,pk=pk)
    context = {"articolo": articolo}
    return render(request, "articolo_detail.html", context)