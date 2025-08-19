from django.contrib import admin
from .models import Post, Comment, Media, Category

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Media)
admin.site.register(Category)
