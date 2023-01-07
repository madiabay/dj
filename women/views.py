from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import Women


# Create your views here.

menu = ['About site', 'Add Post', 'Feedback', 'Login']
def index(request):
    posts = Women.objects.all()

    context = {
        'title': 'Madi site',
        'body': 'Madi body',
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'women/index.html', context)


def cats(request, cat_id):
    if cat_id == 100:
        return redirect('home')
    return HttpResponse(f"<h1>hello cats</h1>\nCategory id is {cat_id}")

def pageNotFound(request, exception):
    return HttpResponseNotFound('Not found ------------------------')
