from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import Women, Category


# Create your views here.

menu = [
    {'title': 'About site', 'url_name': 'about'},
    {'title': 'Add Post', 'url_name': 'add_post'},
    {'title': 'Feedback', 'url_name': 'contact'},
    {'title': 'Login', 'url_name': 'login'},
]
def index(request):
    posts = Women.objects.all()

    context = {
        'title': 'Madi site',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})

def addpost(request):
    return HttpResponse('addpost')

def contact(request):
    return HttpResponse('contact')

def login(request):
    return HttpResponse('login')

def show_post(request, post_id):
    return HttpResponse(f'show_post id->{post_id}')

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': posts,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('Not found ------------------------')
