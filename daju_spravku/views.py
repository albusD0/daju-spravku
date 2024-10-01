from django.shortcuts import render

from django.http import HttpResponse

from django.views import generic

from .models import Article, Category, Tag

from .forms import *


class Home(generic.ListView):
    model = Article

class BlogPost(generic.DetailView):
    model = Article
    form_class = CommentForm

    # def form_valid(self, form): # здесь связывается пост и его автор
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)
    #     # Create Comment object but don't save to database yet
    #     new_comment = comment_form.save(commit=False)
    #     # Assign the current post to the comment
    #     new_comment.post = post

class BlogCategory(generic.DetailView):
    model = Category
    extra_context = {
        'active_category': Category.slug
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_category'] = context['category'].id
        print(context['category'].id)
        return context



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
