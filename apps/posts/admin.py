# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created', 'modified',)
    search_fields = ('title', 'user__username',)
    ordering = ('-created',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created', 'modified',)
    search_fields = ('post__title', 'user__username', 'created', 'description')
    ordering = ('-created',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
