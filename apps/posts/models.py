# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.db import models

from ..users.models import User

from datetime import datetime
import pytz


# Create your models here.


class TimeStampedModel(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, db_index=True)
    description = models.TextField(max_length=512)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    title = models.CharField(max_length=254)
    image = models.ImageField(upload_to='images/posts', blank=True)

    def __unicode__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


class Comment(TimeStampedModel):

    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE, db_index=True)

    def __unicode__(self):
        return '%s %s' % (self.user, self.post)

    def get_absolute_url(self):
        return reverse('posts:post_detail', kwargs={'pk': self.object.post.id, })


'''
class Answer(TimeStampedModel):

    def __unicode__(self):
        return self.user

'''
