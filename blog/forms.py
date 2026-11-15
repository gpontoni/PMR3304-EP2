from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']
        labels = {
            'title': 'Título',
            'content': 'Conteúdo (pode usar HTML)',
            'categories': 'Categorias',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 12}),
            'categories': forms.CheckboxSelectMultiple(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Seu comentário'}
        widgets = {'text': forms.Textarea(attrs={'rows': 4})}