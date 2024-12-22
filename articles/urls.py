from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
    path('creer/', views.creer_article, name='creer_article'),
    path('<int:article_id>/modifier/', views.modifier_article, name='modifier_article'),
    path('<int:article_id>/supprimer/', views.supprimer_article, name='supprimer_article'),
]