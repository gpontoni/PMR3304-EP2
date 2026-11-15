from django.contrib import admin
from .models import Answer, Question

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'theme', 'author', 'date_posted')
    list_filter = ('theme',)
    search_fields = ('title', 'text')
    inlines = [AnswerInline]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'date_posted')
    list_filter = ('author',)