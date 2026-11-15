from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Cria o modelo para Category
class Category(models.Model):
    name = models.CharField('nome', max_length=100)
    description = models.TextField('descrição')

    class Meta:
        ordering = ['name']
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category_detail', kwargs={'pk': self.pk})


# Cria o modelo para Post
class Post(models.Model):
    title = models.CharField('título', max_length=200)
    content = models.TextField('conteúdo')
    date_posted = models.DateTimeField('data de postagem', default=timezone.now)
    categories = models.ManyToManyField(
        Category, related_name='posts', blank=True, verbose_name='categorias'
    )

    class Meta:
        ordering = ['-date_posted']
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})


# Cria o modelo para Comment
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments', verbose_name='post'
    )
    # Referência ao modelo User
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='autor',
    )
    text = models.TextField('texto')
    date_posted = models.DateTimeField('data de postagem', default=timezone.now)

    class Meta:
        ordering = ['-date_posted']  # mais recente primeiro
        verbose_name = 'comentário'
        verbose_name_plural = 'comentários'

    def __str__(self):
        return f'{self.author} em "{self.post}"'