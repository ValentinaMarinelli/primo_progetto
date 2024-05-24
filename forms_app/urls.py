from django.urls import path
from forms_app.views import *

app_name="forms_app"
urlpatterns = [
    path('contattaci/', contatti, name='contatti'),
    path('', index_contatto, name='index_contatto'),
    path('lista_contatti/', lista_contatti, name='lista_contatti'),
    path('modifica_contatto/<int:pk>', modifica_contatto, name='modifica_contatto'),
    path('elimina_contatto/<int:pk>', elimina_contatto, name='elimina_contatto'),
]
