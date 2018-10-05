from django import forms

from .models import Post, Comment
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
            'text': TinyMCE(attrs={'cols': 40, 'rows': 30}),
        }
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)