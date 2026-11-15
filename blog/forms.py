from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': 'Título',
            'content': 'Conteúdo (pode usar HTML)',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 12}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Seu comentário'}
        widgets = {'text': forms.Textarea(attrs={'rows': 4})}