from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path('post/<slug:slug>/', views.BlogPost.as_view(), name='post'),
    path('category/<slug:slug>/', views.BlogCategory.as_view(), name='category'),
    path('tag/<slug:slug>/', views.BlogTag.as_view(), name='tag'),
]