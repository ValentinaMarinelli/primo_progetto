from django.shortcuts import render, get_object_or_404
from .models import Articolo, Giornalista
import datetime

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

def listaArticoli(request,pk=None):
    if(pk==None):
        articoli = Articolo.objects.all()
    else:
        articoli = Articolo.objects.filter(giornalista_id=pk)
    context = {
        'articoli' : articoli,
        'pk' : pk,
    }
    return render(request,'lista_articoli.html',context)

def queryBase(request):
    #1. Tutti gli articoli scritti da giornalisti di un certo cognome:
    articoli_cognome = Articolo.objects.filter(giornalista_cognome='Bianchi')
    #2. Totale
    numero_totale_articoli = Articolo.objects.count()

    #3. Contare il numero di articoli scritti da un giornalista specifico:
    giornalista_1 = Giornalista.objects.get(id=1)
    numero_articoli_giornalista_1 = Articolo.objects.filter(giornalista = giornalista_1).count()

    #4. Ordinare gli articoli per numero di visualizzazione in ordine decrescente:
    articoli_ordinati = Articolo.objects.order_by('-visualizzazioni')

    #5. Tutti gli articoli che non vanno visualizzati
    articoli_senza_visualizzazioni = Articolo.objects.filter(visualizzazioni=0)

    #6. Articolo più visualizzato
    articoli_piu_visualizzato = Articolo.objects.order_by('-visualizzazioni').first()

    #7. Tutti i giornalisti nati dopo una certa data:
    giornalisti_data = Giornalista.objects.filter(anno_di_nascita__gt=datetime.date(1990,1,1))

    #8. Tutti gli articoli pubblicati in una data specifica:
    articoli_del_giorno = Articolo.objects.filter(data=datetime.date(2023,1,1))

    #9. Tutti gli articoli pubblicati in un intervallo di date
    articoli_periodo = Articolo.objects.filter(data__range=(datetime.date(2023,1,1),datetime.date(2023,12,31)))

    #10. Gli articoli scritti da giornalisti nati prima del 1980:
    giornalisti_nati = Giornalista.objects.filter(anno_di_nascita__lt=datetime.date(1980,1,1))
    articoli_giornalisti = Articolo.objects.filter(giornalista__in=giornalisti_nati)

    #11. Il giornalista più giovane:
    giornalista_giovane = Giornalista.objects.order_by('anno_di_nascita').first()

    #12. Il giornalista più anziano
    giornalista_anziano = Giornalista.objects.order_by('-anno_di_nascita').first()

    #13. Gli ultimi 5 articoli pubblicati
    ultimi = Articolo.objects.order_by('-data')[:5]

    #14. Tutti gli articoli con un certo numero minimo di visualizzazioni:
    articoli_minime_visualizzazioni = Articolo.objects.filter(visualizzazioni__gte=100)

    #15. Tutti gli articoli che contengono una certa parola nel titolo:
    articoli_parola = Articolo.objects.filter(titolo__icontains='importante')
    #Creare il dizionario context:
    context = {
        'articoli_cognome': articoli_cognome,
        'numero_totale_articoli' : numero_totale_articoli,
        'numero_articoli_giornalista_1' : numero_articoli_giornalista_1,
        'articoli_ordinati' : articoli_ordinati,
        'articoli_senza_visualizzazioni' : articoli_senza_visualizzazioni,
        'articolo_piu_visualizzato': articoli_piu_visualizzato,
        'giornalisti_data' : giornalisti_data,
        'articoli_del_giorno' : articoli_del_giorno,
        'articoli_periodo' : articoli_periodo,
        'articoli_giornalisti' : articoli_giornalisti,
        'giornalista_giovane' : giornalista_giovane,
        'giornalista_anziano' : giornalista_anziano,
        'ultimi' : ultimi,
        'articoli_minime_visualizzazioni' : articoli_minime_visualizzazioni,
        'articoli_parola' : articoli_parola,
    }