from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Username da conta da Stella (as respostas dela são destacadas)
STELLA_USERNAME = 'stella'

# Modelo para perguntas
class Question(models.Model):
    THEMES = [
        ('moda', 'Moda'),
        ('trends', 'Trends'),
        ('magia', 'Magia'),
        ('transformacoes', 'Transformações'),
    ]

    title = models.CharField('título', max_length=200)
    theme = models.CharField('tema', max_length=20, choices=THEMES, default='moda')
    text = models.TextField('pergunta')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='autora',
    )
    date_posted = models.DateTimeField('data de postagem', default=timezone.now)

    class Meta:
        ordering = ['-date_posted']
        verbose_name = 'pergunta'
        verbose_name_plural = 'perguntas'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum:detail', kwargs={'pk': self.pk})

    def answered_by_stella(self):
        return self.answers.filter(author__username=STELLA_USERNAME).exists()

# Modelo para respostas
class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers', verbose_name='pergunta'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='autor',
    )
    text = models.TextField('resposta')
    date_posted = models.DateTimeField('data de postagem', default=timezone.now)

    class Meta:
        ordering = ['date_posted']  # mais antiga primeiro
        verbose_name = 'resposta'
        verbose_name_plural = 'respostas'

    def __str__(self):
        return f'{self.author} em "{self.question}"'

    def is_from_stella(self):
        return self.author.username == STELLA_USERNAME