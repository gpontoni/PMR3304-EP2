import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='título')),
                ('theme', models.CharField(choices=[('moda', 'Moda'), ('trends', 'Trends'), ('magia', 'Magia'), ('transformacoes', 'Transformações')], default='moda', max_length=20, verbose_name='tema')),
                ('text', models.TextField(verbose_name='pergunta')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now, verbose_name='data de postagem')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL, verbose_name='autora')),
            ],
            options={
                'verbose_name': 'pergunta',
                'verbose_name_plural': 'perguntas',
                'ordering': ['-date_posted'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='resposta')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now, verbose_name='data de postagem')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL, verbose_name='autor')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='forum.question', verbose_name='pergunta')),
            ],
            options={
                'verbose_name': 'resposta',
                'verbose_name_plural': 'respostas',
                'ordering': ['date_posted'],
            },
        ),
    ]