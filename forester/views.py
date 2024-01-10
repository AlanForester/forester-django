# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView

from apps.posts.models import Post

from datetime import date, datetime


# Create your views here.

class IndexView(ListView):
    template_name = "index.html"
    queryset = Post.objects.all().order_by('-created')[:3]
    context_object_name = 'posts_list'  # Default: object_list

    def dateYear(self):
        today = date.today()
        return today.year
