from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import Women


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
        'body': 'Madi body',
        'menu': menu,
        'posts': posts,
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
def pageNotFound(request, exception):
    return HttpResponseNotFound('Not found ------------------------')
