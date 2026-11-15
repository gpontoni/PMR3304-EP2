from django.urls import path
from . import views

# Namespace
app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),
    path('post/novo/', views.PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('post/<int:pk>/editar/', views.PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/remover/', views.PostDeleteView.as_view(), name='delete'),
    path('post/<int:pk>/comentar/', views.CommentCreateView.as_view(), name='comment_create'),
]