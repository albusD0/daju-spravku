from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('post/<slug:slug>/', views.BlogPost.as_view(), name='post'),
    path('topic/<slug:slug>/', views.BlogCategory.as_view(), name='category'),
    path('tag/<slug:slug>/', views.BlogTag.as_view(), name='tag'),
]