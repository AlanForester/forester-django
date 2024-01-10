# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from apps.posts.api.serializers import (
    PostListSerializer,
    )

from ..models import User


class UserListSerializer(serializers.ModelSerializer):

    posts = PostListSerializer(source="post_set", many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'description',
                  'image',
                  'posts',
                  )


class UserRetrieveSerializer(serializers.ModelSerializer):

    posts = PostListSerializer(source="post_set", many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'description',
                  'image',
                  'posts',
                  )


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'description',
                  'image',
                  )


class UserDeleteSerializer(serializers.ModelSerializer):

    posts = PostListSerializer(source="post_set", many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'description',
                  'image',
                  'posts',
                  )



