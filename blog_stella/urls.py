# ------ Mapa de URLs do site ------

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('sobre/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('diario/', include('blog.urls')),
    path('forum/', include('forum.urls')),
    path('contas/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]