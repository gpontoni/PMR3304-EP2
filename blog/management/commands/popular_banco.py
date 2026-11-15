"""
Popula o banco com o conteúdo do site (e com os dados da parte 4).

Cria:
- a conta de administradora (superusuária) "tecna" (se ainda não existir)
- as contas da Stella, das Winx e de três seguidoras
- 4 categorias e 6 posts do diário
- comentários nos posts
- perguntas e respostas no fórum
"""

import os
from datetime import datetime
from zoneinfo import ZoneInfo
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from blog.models import Category, Comment, Post
from forum.models import Answer, Question

TZ = ZoneInfo('America/Sao_Paulo')

def data(mes, dia, hora, minuto=0):
    return datetime(2026, mes, dia, hora, minuto, tzinfo=TZ)

# Como as imagens do EP1 foram reaproveitadas, elas já se encontram armazenadas localmente
IMAGE_BASE = '/static/images/formas'

ADMIN_USERNAME = 'tecna'
ADMIN_SENHA_PADRAO = 'solaria2026'      # senha da superusuária 'tecna' (administradora do site)
SENHA_USUARIAS = 'winxclub2026'         # senha de todas as outras contas

USUARIAS = ['stella', 'bloom', 'flora', 'musa', 'aisha',
            'amanda_fada', 'lili_magix', 'bia_solaria']

CATEGORIAS = {
    'Transformações': 'Cada nova forma de fada que eu conquistei, contada no dia em que aconteceu.',
    'Moda': 'Looks, acessórios e tudo o que faz uma fada brilhar por fora.',
    'Magia': 'Feitiços, poderes de luz solar e curiosidades sobre a magia de Solária.',
    'Trends': 'O que está bombando agora em Magix (e o que já saiu de moda).',
}

def img(arquivo, alt):
    return f'<img src="{IMAGE_BASE}/{arquivo}" alt="{alt}" class="img-transformacao">\n'

POSTS = [
    {
        'title': 'Minha primeira transformação: Winx',
        'date': data(9, 1, 18, 27),
        'categories': ['Transformações', 'Magia'],
        'content': img('stella_winx.png', 'Stella Winx') +
            '<p>Diário, hoje foi O dia! Me transformei oficialmente em fada pela primeira vez. ☀️</p>\n'
            '<p>Essa é a minha forma básica: com o lendário <strong>Anel de Solaria</strong> eu canalizo rajadas '
            'de luz solar e energia estelar contra qualquer bruxa que cruzar o meu caminho. E, claro, o look já '
            'nasceu impecável.</p>',
        'comments': [
            ('bloom', 'Foi aqui que tudo começou! Lembro do primeiro dia em Alfea. 🔥', data(9, 1, 19, 5)),
            ('tecna', 'Análise: o Anel de Solaria aumenta a potência do raio de luz em cerca de 200%.', data(9, 2, 8, 40)),
            ('amanda_fada', 'Stella, você estava linda mesmo na forma básica! 😍', data(9, 3, 14, 12)),
        ],
    },
    {
        'title': 'Conquistei o Charmix!',
        'date': data(9, 15, 18, 28),
        'categories': ['Transformações', 'Moda'],
        'content': img('stella_charmix.png', 'Stella Charmix') +
            '<p>Gente, eu ganhei o <strong>Charmix</strong>! Ele veio depois que eu finalmente superei as minhas '
            'inseguranças e aprendi a confiar em mim mesma e nas minhas amigas. 🥹</p>\n'
            '<p>Ganhei um broche em forma de espelho (perfeito, né?) e uma bolsinha na cintura que potencializa '
            'os meus poderes. Magia E acessório: o sonho de qualquer estilista.</p>',
        'comments': [
            ('musa', 'Esse broche de espelho é a sua cara! 🎵', data(9, 15, 20, 0)),
            ('lili_magix', 'Onde compra essa bolsinha?? Preciso! 👛', data(9, 16, 9, 30)),
        ],
    },
    {
        'title': 'Enchantix: a noite em que salvei meu pai',
        'date': data(10, 1, 22, 10),
        'categories': ['Transformações', 'Magia'],
        'content': img('stella_enchantix.png', 'Stella Enchantix') +
            '<p>Ainda estou tremendo enquanto escrevo. Em Eraklyon, arrisquei a minha própria vida para salvar o '
            'meu pai, o <strong>Rei Radius</strong>, e foi aí que conquistei o <strong>Enchantix</strong>, a forma '
            'suprema de fada guardiã.</p>\n'
            '<p>As asas são gigantescas e agora eu tenho o Pó de Fada, capaz de quebrar feitiços das trevas. '
            'Papai está bem, e é isso que importa. 💛</p>',
        'comments': [
            ('aisha', 'Que coragem! O Rei Radius deve estar muito orgulhoso. 🌊', data(10, 1, 23, 15)),
            ('bloom', 'Uma das noites mais emocionantes de todas. 😭', data(10, 2, 10, 2)),
        ],
    },
    {
        'title': 'Believix chegou (e é pura alta-costura)',
        'date': data(10, 15, 18, 28),
        'categories': ['Transformações', 'Moda'],
        'content': img('stella_believix.png', 'Stella Believix') +
            '<p>Missão cumprida na Terra: fizemos os humanos voltarem a acreditar em magia, e de presente veio o '
            '<strong>Believix</strong>! ✨</p>\n'
            '<p>Ele amplifica a minha conexão com as emoções das pessoas, me deu asas novas de velocidade e '
            'teletransporte e, sinceramente, o visual parece saído de um desfile de alta-costura.</p>',
        'comments': [
            ('tecna', 'O teletransporte das asas Believix ainda desafia as leis da física. 🤖', data(10, 15, 19, 45)),
            ('flora', 'Fazer os humanos acreditarem de novo foi lindo! 🌷', data(10, 16, 11, 20)),
            ('bia_solaria', 'Esse look é o meu favorito de todos!! 💖', data(10, 17, 16, 50)),
        ],
    },
    {
        # Post sem comentários (parte 4)
        'title': 'Sirenix: brilhando no fundo do mar',
        'date': data(10, 29, 18, 28),
        'categories': ['Transformações', 'Magia'],
        'content': img('stella_sirenix.png', 'Stella Sirenix') +
            '<p>Quem diria que a fada do Sol ia brilhar debaixo d\'água? Conquistei o <strong>Sirenix</strong>, '
            'a transformação ancestral dos mares! 🧜‍♀️</p>\n'
            '<p>Agora eu nado em altas velocidades e uso meus poderes de luz solar sob as águas do Oceano Infinito '
            'para proteger os reinos aquáticos. Meu cabelo continua perfeito, aliás.</p>',
        'comments': [],
    },
    {
        'title': 'Trend da estação: dourado de Solária',
        'date': data(11, 10, 15, 0),
        'categories': ['Moda', 'Trends'],
        'content':
            '<p>Anotem: a trend deste fim de ano em Magix é o <strong>dourado de Solária</strong>! 💛</p>\n'
            '<ul>\n'
            '<li>Brilho dourado nos olhos (pouco é bobagem);</li>\n'
            '<li>Acessórios em forma de sol e de estrela;</li>\n'
            '<li>Tons de rosa e creme para equilibrar o look.</li>\n'
            '</ul>\n'
            '<p>E, por favor: nada de cinza. Estou olhando pra você, Tecna. 😜</p>',
        'comments': [
            ('tecna', 'Registro: o cinza é uma cor neutra e altamente funcional.', data(11, 10, 16, 3)),
            ('amanda_fada', 'Já comprei meus brincos de sol! ☀️', data(11, 11, 9, 41)),
        ],
    },
]

PERGUNTAS = [
    {
        'author': 'amanda_fada', 'theme': 'trends', 'date': data(11, 2, 10, 15),
        'title': 'Qual a trend de inverno em Magix?',
        'text': 'Stella, vai esfriar em Magix e eu não sei o que usar. O que está em alta?',
        'answers': [
            ('stella', 'Amanda, aposte em casacos creme com detalhes dourados! E um cachecol rosa para dar aquele toque de Solária. ❄️✨', data(11, 2, 14, 0)),
            ('lili_magix', 'Eu usei a dica e amei!!', data(11, 3, 9, 12)),
        ],
    },
    {
        'author': 'lili_magix', 'theme': 'transformacoes', 'date': data(11, 5, 19, 30),
        'title': 'Como você conseguiu o Enchantix?',
        'text': 'Sempre quis saber como foi o momento exato da transformação. Doeu?',
        'answers': [
            ('stella', 'Não doeu, Lili! Foi uma onda de luz quentinha. O Enchantix vem quando você se sacrifica por alguém do seu reino. Contei tudo no meu diário! 💛', data(11, 6, 11, 20)),
        ],
    },
    {
        'author': 'bia_solaria', 'theme': 'moda', 'date': data(11, 8, 13, 5),
        'title': 'Dica de acessório para a primeira festa em Alfea?',
        'text': 'Vou na minha primeira festa em Alfea e quero chegar arrasando. Qual acessório não pode faltar?',
        'answers': [
            ('stella', 'Um anel statement! Não precisa ser o de Solária (esse é só meu 😜), mas um anel brilhante muda qualquer look.', data(11, 8, 17, 45)),
            ('flora', 'E uma flor no cabelo também fica lindo! 🌸', data(11, 9, 10, 0)),
        ],
    },
    {
        # Pergunta ainda sem resposta da Stella (para responder manualmente e demonstrar funcionamento do site)
        'author': 'lili_magix', 'theme': 'magia', 'date': data(11, 13, 21, 0),
        'title': 'O Anel de Solaria precisa de recarga?',
        'text': 'Fiquei curiosa: o anel funciona à noite, sem sol?',
        'answers': [],
    },
]


class Command(BaseCommand):
    help = 'Popula o banco com o conteúdo do site, usuários, comentários e o fórum.'

    def handle(self, *args, **options):
        User = get_user_model()

        # --- Conta de administradora (Tecna) ---
        senha_admin = os.environ.get('ADMIN_PASSWORD')
        if not senha_admin and 'RENDER' not in os.environ:
            senha_admin = ADMIN_SENHA_PADRAO
        if senha_admin and not User.objects.filter(username=ADMIN_USERNAME).exists():
            User.objects.create_superuser(ADMIN_USERNAME, '', senha_admin)
            self.stdout.write(f'Superusuária criada: {ADMIN_USERNAME}')
        elif not senha_admin:
            self.stdout.write(self.style.WARNING(
                'ADMIN_PASSWORD não definida: superusuária não criada.'))

        # --- Demais contas ---
        usuarios = {ADMIN_USERNAME: User.objects.filter(username=ADMIN_USERNAME).first()}
        for username in USUARIAS:
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password(SENHA_USUARIAS)
                user.save()
            usuarios[username] = user

        # --- Categorias ---
        categorias = {}
        for name, description in CATEGORIAS.items():
            cat, _ = Category.objects.get_or_create(name=name, defaults={'description': description})
            categorias[name] = cat

        # --- Posts do diário e comentários ---
        for dados in POSTS:
            post, _ = Post.objects.get_or_create(
                title=dados['title'],
                defaults={'content': dados['content'], 'date_posted': dados['date']},
            )
            post.categories.set([categorias[c] for c in dados['categories']])
            if not post.comments.exists():
                for username, text, date in dados['comments']:
                    if usuarios.get(username):
                        Comment.objects.create(post=post, author=usuarios[username],
                                               text=text, date_posted=date)

        # --- Fórum ---
        for dados in PERGUNTAS:
            question, created = Question.objects.get_or_create(
                title=dados['title'],
                defaults={'text': dados['text'], 'theme': dados['theme'],
                          'author': usuarios[dados['author']], 'date_posted': dados['date']},
            )
            if created:
                for username, text, date in dados['answers']:
                    Answer.objects.create(question=question, author=usuarios[username],
                                          text=text, date_posted=date)

        self.stdout.write(self.style.SUCCESS(
            f'Pronto! {Post.objects.count()} posts, {Category.objects.count()} categorias, '
            f'{Comment.objects.count()} comentários e {Question.objects.count()} perguntas no fórum.'
        ))