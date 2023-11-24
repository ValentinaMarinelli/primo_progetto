from django.urls import path
from news.views import *

app_name = 'news'

urlpatterns = [
    path("homepage_news", home, name="homepage_news"),
    path("articoli/", articoloDetailView, name = "articolo_detail"),
    path("articoli/<int:pk>", articoloDetailView, name = "articolo_detail"),
    path("giornalisti/", giornalistaDetailVieW, name = "giornalista_detail"),
    path("giornalisti/<int:pk>", giornalistaDetailVieW, name = "giornalista_detail"),
    path("lista_articoli/<int:pk>", listaArticoli, name = "lista_articoli"),
    path("lista_articoli/", listaArticoli, name = "lista_articoli"),
    path("lista_giornalisti/<int:pk>", listaGiornalisti, name = "lista_giornalisti"),
    path("lista_giornalisti/", listaGiornalisti, name = "lista_giornalisti"),
    path("query/", queryBase, name = "query"),
    path('', index_news, name='index_news'),
]
