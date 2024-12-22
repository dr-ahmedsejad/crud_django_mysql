from django.shortcuts import render, redirect, get_object_or_404
from .models import Auteur

def liste_auteurs(request):
    auteurs = Auteur.objects.all()
    return render(request, 'liste.html', {'auteurs': auteurs})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Auteur
from .forms import AuteurForm

# Lister les auteurs
def liste_auteurs(request):
    auteurs = Auteur.objects.all()
    return render(request, 'liste_auteur.html', {'auteurs': auteurs})

# Créer un auteur
def creer_auteur(request):
    if request.method == 'POST':
        form = AuteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_auteurs')
    else:
        form = AuteurForm()
    return render(request, 'creer_auteur.html', {'form': form})

# Modifier un auteur
def modifier_auteur(request, auteur_id):
    auteur = get_object_or_404(Auteur, id=auteur_id)
    if request.method == 'POST':
        form = AuteurForm(request.POST, instance=auteur)
        if form.is_valid():
            form.save()
            return redirect('liste_auteurs')
    else:
        form = AuteurForm(instance=auteur)
    return render(request, 'modifier_auteur.html', {'form': form, 'auteur': auteur})

# Supprimer un auteur
def supprimer_auteur(request, auteur_id):
    auteur = get_object_or_404(Auteur, id=auteur_id)
    if request.method == 'POST':
        auteur.delete()
        return redirect('liste_auteurs')
    return render(request, 'supprimer_auteur.html', {'auteur': auteur})

