from django.contrib import admin
from django import forms

from .models import Article, Category, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.

class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'content')
    prepopulated_fields = {'slug': ('title',),}
    form = ArticleAdminForm

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',),}

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ''('user', 'post', 'created')''

admin.site.register(Comment)
