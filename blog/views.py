from django.urls import reverse_lazy
from django.views import generic
from .forms import PostForm
from .models import Post

# template padrão: blog/post_list.html
class PostListView(generic.ListView):
    model = Post

# template padrão: blog/post_detail.html
class PostDetailView(generic.DetailView):
    model = Post
    # DetailView já responde com 404 se o post não existirgi

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