from django.urls import path
from voti.views import *

app_name = 'voti'

urlpatterns = [
    path("lista_materie", view_a, name="lista_materie"),
    path("voti_studenti", view_b, name = "voti_studenti"),
    path("media_studenti", view_c, name = "media_studenti"),
    path("max_min_voti", view_d, name = "max_min_voti"),
    path('', index_voti, name='index_voti'),
]
