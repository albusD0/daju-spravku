from django.shortcuts import render

from django.http import HttpResponse

from django.views import generic

from .models import Article, Category, Tag


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class Home(generic.ListView):
    model = Article

class BlogPost(generic.DetailView):
    model = Article

class BlogCategory(generic.ListView):
    model = Category

class BlogTag(generic.ListView):
    model = Tag
