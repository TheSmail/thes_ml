from django.contrib import admin

from .models import Post
from .forms import PostForm
# Register your models here.

admin.site.register(Post)
# @admin.register(Post)
# class PostModelAdmin(admin.ModelAdmin):
#     form = PostForm
