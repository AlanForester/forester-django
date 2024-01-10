# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    )

from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    )

from .serializers import (
    PostListSerializer,
    PostRetrieveSerializer,
    PostCreateSerializer,
    PostUpdateSerializer,
    PostDeleteSerializer,
    CommentListSerializer,
    CommentRetrieveSerializer,
    CommentCreateSerializer,
    CommentUpdateSerializer,
    CommentDeleteSerializer,
    )

from ..models import Post, Comment

# Create your views here.

# Posts #


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()  # It is not necessary
    serializer_class = PostCreateSerializer


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer


class PostDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDeleteSerializer


# Comments #


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer


class CommentRetrieveAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentRetrieveSerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()  # It is not necessary
    serializer_class = CommentCreateSerializer


class CommentUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer


class CommentDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteSerializer



