from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article

# Create your views here.
def index(request):
    post_list = Article.objects.all()
    return render(request, 'index.html', {'post_list': post_list})

def about_me(request):
    return render(request, 'about_me.html')

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})

def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list': post_list, 'error': False})

def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(tag__iexact = tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list':post_list})

def cypto(request):
    return render(request, 'cypto.html')

