from django import forms
from .models import Article, Image

# class ArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ['titre', 'contenu', 'categorie', 'auteur']
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'categorie', 'auteur']
        widgets = {
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez le titre de l\'article',
            }),
            'contenu': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Rédigez le contenu de l\'article ici...',
            }),
            'categorie': forms.Select(attrs={
                'class': 'form-select',
            }),
            'auteur': forms.Select(attrs={
                'class': 'form-select',
            }),
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
