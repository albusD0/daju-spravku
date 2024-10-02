from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.urls import reverse

from django.views import generic
from django.views.generic import CreateView, FormView

from .models import Article, Category, Tag

from .forms import *


class Home(generic.ListView):
    model = Article

class BlogPost(generic.DetailView, generic.FormView):
    model = Article
    form_class = CommentForm

    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        return reverse('post', kwargs={'slug': self.kwargs['slug'], })

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        # возвращаем form_valid предка
        return super().form_valid(form)



    # def form_valid(self, form): # здесь связывается пост и его автор
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)
    #     # Create Comment object but don't save to database yet
    #     new_comment = comment_form.save(commit=False)
    #     # Assign the current post to the comment
    #     new_comment.post = post

class BlogCategory(generic.DetailView):
    model = Category


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


class BlogCommentCreate(LoginRequiredMixin, CreateView):
    """
    Form for adding a blog comment. Requires login.
    """
    model = Comment
    fields = ['content', ]

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        # Get the blog from slug and add it to the context
        context['article'] = get_object_or_404(Article, slug=self.kwargs['slug'])
        return context

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        # Add logged-in user as author of comment
        form.instance.author = self.request.user
        # Associate comment with blog based on passed id
        form.instance.blog = get_object_or_404(Article, slug=self.kwargs['slug'])
        # Call super-class form validation behaviour
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        return reverse('post', kwargs={'slug': self.kwargs['slug'], })