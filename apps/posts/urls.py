"""
forester URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include

from .views import PostListView
from .views import PostCreateView, PostDetailView, PostUpdateView, PostDeleteView
from .views import CommentCreateView, CommentDeleteView, CommentUpdateView

app_name = 'posts'

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^post/add/$', PostCreateView.as_view(), name='post_add'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^post/(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='post_update_form'),
    url(r'^post/(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='post_delete'),
    url(r'^post/(?P<pk>\d+)/comment/add/$', CommentCreateView.as_view(), name='comment_add'),
    url(r'^comments/(?P<pk>\d+)/delete/$', CommentDeleteView.as_view(), name='comment_delete'),
    url(r'^comments/(?P<pk>\d+)/update/$', CommentUpdateView.as_view(), name='comment_update_form'),

]
