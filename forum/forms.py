from django import forms
from .models import Answer, Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'theme', 'text']
        labels = {
            'title': 'Título da pergunta',
            'theme': 'Tema',
            'text': 'Sua pergunta para a Stella',
        }
        widgets = {'text': forms.Textarea(attrs={'rows': 6})}

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']
        labels = {'text': 'Sua resposta'}
        widgets = {'text': forms.Textarea(attrs={'rows': 4})}