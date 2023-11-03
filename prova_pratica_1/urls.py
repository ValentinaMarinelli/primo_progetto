from django.urls import path
from prova_pratica_1.views import *

app_name="prova_pratica_1"
urlpatterns=[
    path('', index_prova1, name='index_prova1'),
    path('maxmin', maxmin, name='maxmin'),
    path('media', media, name='media'),
    path('voti', voti, name='voti'),
]