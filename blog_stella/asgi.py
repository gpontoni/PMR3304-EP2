#Configuração ASGI do projeto blog_stella
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_stella.settings')

application = get_asgi_application()