from django.shortcuts import render, redirect, get_object_or_404
from .models import Categorie

def liste_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'liste_categorie.html', {'categories': categories})

