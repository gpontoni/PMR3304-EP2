from django import forms
from .models import Post

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