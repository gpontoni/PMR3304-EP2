from django.contrib import admin
from .models import Category, Comment, Post

# Mostra os comentários dentro da página do post no admin
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')
    list_filter = ('categories',)
    search_fields = ('title', 'content')
    filter_horizontal = ('categories',)
    inlines = [CommentInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'date_posted')
    list_filter = ('post', 'author')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)