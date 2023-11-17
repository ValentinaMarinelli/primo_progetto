from django.urls import path
from news.views import *

app_name = 'news'

urlpatterns = [
    path("homepage_news", home, name="homepage_news"),
    path("articoli/", articoloDetailView, name = "articolo_detail"),
    path("articoli/<int:pk>", articoloDetailView, name = "articolo_detail"),
    path("lista_articoli/<int:pk>", listaArticoli, name = "lista_articoli"),
    path("lista_articoli/", listaArticoli, name = "lista_articoli"),
    path("query/", queryBase, name = "query"),
    path('', index_news, name='index_news'),
]
