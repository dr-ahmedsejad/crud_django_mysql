from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Image
from .forms import ArticleForm

def liste_articles(request):
    articles = Article.objects.all()
    return render(request, 'liste_article.html', {'articles': articles})

def creer_article(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save()
            # Gérer les images
            images = request.FILES.getlist('images')
            for image in images:
                Image.objects.create(article=article, image=image)
            return redirect('liste_articles')
    else:
        article_form = ArticleForm()
    return render(request, 'creer_article.html', {'article_form': article_form})

# Modifier un article
def modifier_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            # Remplacer les images existantes par de nouvelles
            article.images.all().delete()  # Supprime toutes les images associées
            new_images = request.FILES.getlist('images')  # Récupère les nouvelles images
            for image in new_images:
                Image.objects.create(article=article, image=image)
            return redirect('liste_articles')
    else:
        form = ArticleForm(instance=article)

    return render(request, 'modifier_article.html', {
        'form': form,
        'article': article,
    })
# Supprimer un article
def supprimer_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('liste_articles')
    return render(request, 'supprimer_article.html', {'article': article})