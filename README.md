# Stella de Solária — PMR3304 EP2

Site dinâmico tipo diário (blog) com comentários e categorias, fórum de 
perguntas para a Stella e as páginas Home e Sobre originais.

## Rodando localmente

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py popular_banco   # conteúdo do site + contas
python manage.py runserver
```

- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/ — usuária `tecna`, senha `solaria2026`
- Demais contas (stella, bloom, amanda_fada...): senha `winxclub2026`

## Mapa de URLs

| URL | Nome | O que é |
|---|---|---|
| `/` | `home` | Página de recepção |
| `/sobre/` | `about` | Nota da Tecna |
| `/diario/` | `blog:list` | Lista de posts do diário |
| `/diario/post/novo/` | `blog:create` | Novo post |
| `/diario/post/<pk>/` | `blog:detail` | Post + categorias + comentários |
| `/diario/post/<pk>/editar/` | `blog:update` | Editar post |
| `/diario/post/<pk>/remover/` | `blog:delete` | Confirmar remoção |
| `/diario/post/<pk>/comentar/` | `blog:comment_create` | Novo comentário |
| `/diario/categorias/` | `blog:category_list` | Lista de categorias |
| `/diario/categorias/<pk>/` | `blog:category_detail` | Posts de uma categoria |
| `/forum/` | `forum:list` | Perguntas do fórum |
| `/forum/pergunta/nova/` | `forum:create` | Nova pergunta |
| `/forum/pergunta/<pk>/` | `forum:detail` | Pergunta + respostas |
| `/forum/pergunta/<pk>/responder/` | `forum:answer_create` | Nova resposta |
| `/forum/cadastro/` | `forum:signup` | Cadastro de seguidora |
| `/contas/login/` | `login` | Entrar |

## Deploy no Render

- Build Command: `./build.sh`
- Start Command: `gunicorn blog_stella.wsgi:application`
- Variáveis de ambiente: `SECRET_KEY`, `ADMIN_PASSWORD`