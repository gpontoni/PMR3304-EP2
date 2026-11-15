from django.urls import path
from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.QuestionListView.as_view(), name='list'),
    path('pergunta/nova/', views.QuestionCreateView.as_view(), name='create'),
    path('pergunta/<int:pk>/', views.QuestionDetailView.as_view(), name='detail'),
    path('pergunta/<int:pk>/responder/', views.AnswerCreateView.as_view(), name='answer_create'),
    path('cadastro/', views.SignUpView.as_view(), name='signup'),
]