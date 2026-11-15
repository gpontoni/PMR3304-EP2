from django.db import models
from django.urls import reverse
from django.utils import timezone

# Post do diário da Stella
class Post(models.Model):
    title = models.CharField('título', max_length=200)
    content = models.TextField('conteúdo')
    date_posted = models.DateTimeField('data de postagem', default=timezone.now)

    class Meta:
        ordering = ['-date_posted']
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})