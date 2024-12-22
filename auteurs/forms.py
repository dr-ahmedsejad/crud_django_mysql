from django import forms
from .models import Auteur

class AuteurForm(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = ['nom', 'email','pseudonyme']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez le nom de l\'auteur'
            }),
            'pseudonyme': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez le pseudonyme de l\'auteur'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez l\'adresse email de l\'auteur'
            }),
        }
