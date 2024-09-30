from django.forms import forms

from .models import Comment

class CommentsForm(form.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'text',)