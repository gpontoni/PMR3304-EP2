from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import AnswerForm, QuestionForm
from .models import Answer, Question

# template padrão: forum/question_list.html
class QuestionListView(generic.ListView):
    model = Question

# template padrão: forum/question_detail.html
class QuestionDetailView(generic.DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answer_form'] = AnswerForm()
        return context

# template padrão: forum/question_form.html
class QuestionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Question
    form_class = QuestionForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# template padrão: forum/answer_form.html
class AnswerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Answer
    form_class = AnswerForm

    def dispatch(self, request, *args, **kwargs):
        self.question = get_object_or_404(Question, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = self.question
        return context

    def form_valid(self, form):
        form.instance.question = self.question
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('forum:detail', kwargs={'pk': self.question.pk})

# Cadastro de novas seguidoras
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')