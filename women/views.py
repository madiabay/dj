from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from  django.contrib.auth.mixins import LoginRequiredMixin

#class
from django.views.generic import ListView, DetailView, CreateView

from .models import Women, Category
from .forms import AddPostForm
from .utils import *


# Create your views here.
class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats_def = self.get_user_context(title="Madi's site")
        return dict(list(context.items()) + list(cats_def.items()))

    def get_queryset(self):
        return Women.objects.filter(is_published=True)

# def index(request):
#     posts = Women.objects.all()
#
#     context = {
#         'title': 'Madi site',
#         'menu': menu,
#         'posts': posts,
#         'cat_selected': 0,
#     }
#     return render(request, 'women/index.html', context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(cats_def.items()))


# def addpost(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # try:
#             #     Women.objects.create(**form.cleaned_data)
#             #     return redirect(to='home')
#             # except:
#             #     form.add_error(None, 'Ошибка добавления поста')
#
#             form.save()
#             return redirect(to='home')
#     else:
#         form = AddPostForm()
#
#
#     return render(request,
#                   'women/addpage.html',
#                   {'form': form, 'menu': menu, 'title': 'Добавление статьи'}
#                   )

def contact(request):
    return HttpResponse('contact')

def login(request):
    return HttpResponse('login')


class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats_def = self.get_user_context(title='Пост - ' + str(context['post']))
        return dict(list(context.items()) + list(cats_def.items()))

# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'women/post.html', context)


class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats_def = self.get_user_context(
            title='Категория - ' + str(context['posts'][0].cat),
            cat_selected=context['posts'][0].cat_id
        )
        return dict(list(context.items()) + list(cats_def.items()))

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

# def show_category(request, cat_id):
#     posts = Women.objects.filter(cat=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'title': 'Отображение по рубрикам',
#         'menu': menu,
#         'posts': posts,
#         'cat_selected': cat_id,
#     }
#     return render(request, 'women/index.html', context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('Not found ------------------------')
