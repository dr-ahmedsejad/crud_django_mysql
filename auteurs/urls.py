from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_auteurs, name='liste_auteurs'),
    path('creer/', views.creer_auteur, name='creer_auteur'),
    path('modifier/<int:auteur_id>', views.modifier_auteur, name='modifier_auteur'),
    path('supprimer/<int:auteur_id>', views.supprimer_auteur, name='supprimer_auteur'),
]

