from django.contrib import admin
from article.models import Article
from .templatetags import custom_markdown

# Register your models here.
admin.site.register(Article)
#admin.site.register(custom_markdown)