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

class BlogCategory(generic.DetailView):
    model = Category
    extra_context = {
        'active_category': Category.slug
    }

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(context)
    #     context['active_category'] = Category.objects.filter(self)
    #     print(context)
    #     return context



class BlogTag(generic.ListView):
    model = Tag

class SearchResultsView(generic.ListView):
    model = Article
    template_name = 'daju_spravku/search_results.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('s')
        object_list = Article.objects.filter(title__icontains=query)
        return object_list

    def get_context_data(self, **kwargs):
        query = super().get_context_data(**kwargs)
        query['query'] = self.request.GET.get('s')
        return query
