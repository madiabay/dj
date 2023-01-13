from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import Women, Category
from .forms import AddPostForm


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
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect(to='home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm()


    return render(request,
                  'women/addpage.html',
                  {'form': form, 'menu': menu, 'title': 'Добавление статьи'}
                  )

def contact(request):
    return HttpResponse('contact')

def login(request):
    return HttpResponse('login')

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'women/post.html', context)

def show_category(request, cat_id):
    posts = Women.objects.filter(id=cat_id)

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
