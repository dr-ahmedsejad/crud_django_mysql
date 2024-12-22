from django.db import models
from categories.models import Categorie
from auteurs.models import Auteur

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='articles')
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE, related_name='articles')
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

class Image(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='articles/images/')

    def __str__(self):
        return f"Image de {self.article.titre}"

