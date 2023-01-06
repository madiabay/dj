from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return HttpResponse('hello world')


def cats(request, cat_id):
    if cat_id == 100:
        return redirect('home')
    return HttpResponse(f"<h1>hello cats</h1>\nCategory id is {cat_id}")

def pageNotFound(request, exception):
    return HttpResponseNotFound('Not found ------------------------')
