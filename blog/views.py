from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import CommentForm, PostForm
from .models import Category, Comment, Post

# ---------- Posts ----------

# template padrão: blog/post_list.html
class PostListView(generic.ListView):
    model = Post

# template padrão: blog/post_detail.html
class PostDetailView(generic.DetailView):
    model = Post
    # a DetailView já responde com 404 se o post não existir

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

# template padrão: blog/post_form.html
class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    # depois de salvar, redireciona para post.get_absolute_url()

class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm

# template padrão: blog/post_confirm_delete.html
class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list')


# ---------- Comentários ----------

# Cria um comentário no post da URL (só para quem está logado)
class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    # Busca o post da URL (404 se não existir)
    def dispatch(self, request, *args, **kwargs):
        self.post_obj = get_object_or_404(Post, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.post_obj
        return context

    def form_valid(self, form):
        form.instance.post = self.post_obj
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'pk': self.post_obj.pk})


# ---------- Categorias ----------

# template padrão: blog/category_list.html
class CategoryListView(generic.ListView):
    model = Category

# Reaproveita o template de listagem de posts da parte 1
class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'blog/post_list.html'
    # a DetailView já responde com 404 se a categoria não existir

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = self.object.posts.all()
        return context