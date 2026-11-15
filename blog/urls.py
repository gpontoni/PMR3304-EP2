from django.urls import path
from . import views

# Namespace
app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='list'),
    path('post/novo/', views.post_create, name='create'),
    path('post/<int:pk>/', views.post_detail, name='detail'),
    path('post/<int:pk>/editar/', views.post_update, name='update'),
    path('post/<int:pk>/remover/', views.post_delete, name='delete'),
]