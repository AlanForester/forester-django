# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from ..models import Post, Comment

# Comment #


class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id',
                  'description',
                  'user',
                  'post',
                  )


class CommentRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id',
                  'description',
                  'user',
                  'post',
                  )


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id',
                  'description',
                  'user',
                  'post',
                  )


class CommentUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id',
                  'description',
                  'user',
                  'post',
                  )


class CommentDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id',
                  'description',
                  'user',
                  'post',
                  )


# Posts #

class PostListSerializer(serializers.ModelSerializer):

    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id',
                  'title',
                  'description',
                  'user',
                  'image',
                  'comments',
                  )


class PostRetrieveSerializer(serializers.ModelSerializer):

    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id',
                  'title',
                  'description',
                  'user',
                  'image',
                  'comments',
                  )


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id',
                  'title',
                  'description',
                  'image',
                  'user',
                  )


class PostUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id',
                  'title',
                  'description',
                  'image',
                  'user',
                  )


class PostDeleteSerializer(serializers.ModelSerializer):

    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id',
                  'title',
                  'description',
                  'image',
                  'user',
                  'comments',
                  )




