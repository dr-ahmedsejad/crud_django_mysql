from django.db import models

class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    pseudonyme = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nom

