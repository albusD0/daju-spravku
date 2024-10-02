from django.forms import ModelForm, CharField

from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'content')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["author"].widget.attrs.update({"class": "col-sm-10"})
    #     self.fields["content"].widget.attrs.update({"class": "col-sm-10"})


