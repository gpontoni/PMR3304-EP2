# Stella de Solária — PMR3304 EP2

Versão dinâmica (Django) do portfólio em Hugo do EP1: diário (blog) com
comentários e categorias, fórum de perguntas para a Stella e as páginas
Home e Sobre originais.

## Rodando localmente

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Acesse http://127.0.0.1:8000/
