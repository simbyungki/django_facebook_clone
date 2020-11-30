from django.contrib import admin
from facebook.models import Article, Page, Comment

class ArticleView(admin.ModelAdmin) :
    list_display = ('title', 'author', 'created_at')

class CommentView(admin.ModelAdmin) :
    list_display = ('article', 'author', 'text', 'created_at')

admin.site.register(Article, ArticleView)
admin.site.register(Page)
admin.site.register(Comment, CommentView)