
from django.conf.urls import url, include

from .views import (
    PostListAPIView,
    PostRetrieveAPIView,
    PostCreateAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
    CommentListAPIView,
    CommentRetrieveAPIView,
    CommentCreateAPIView,
    CommentUpdateAPIView,
    CommentDeleteAPIView,
    )

app_name = 'posts'

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='post-list'),
    url(r'^post/add/$', PostCreateAPIView.as_view(), name='post-add'),
    url(r'^post/(?P<pk>\d+)/$', PostRetrieveAPIView.as_view(), name='post-detail'),
    url(r'^post/(?P<pk>\d+)/update/$', PostUpdateAPIView.as_view(), name='post-update'),
    url(r'^post/(?P<pk>\d+)/delete/$', PostDeleteAPIView.as_view(), name='post-delete'),
    url(r'^comment/$', CommentListAPIView.as_view(), name='comment-list'),
    url(r'^comment/(?P<pk>\d+)/$', CommentRetrieveAPIView.as_view(), name='comment-detail'),
    url(r'^post/(?P<pk>\d+)/comment/add/$', CommentCreateAPIView.as_view(), name='comment_add'),
    url(r'^comment/(?P<pk>\d+)/update/$', CommentUpdateAPIView.as_view(), name='comment-update'),
    url(r'^comment/(?P<pk>\d+)/delete/$', CommentDeleteAPIView.as_view(), name='comment-delete'),

]

