# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm, CommentForm
from .models import Post, Comment


# Create your views here.


class PostListView(LoginRequiredMixin, ListView):
    model = Post  # Equals: queryset = Post.objects.all()
    template_name = 'posts/post_list.html'  # Default: <app_label>/<model_name>_list.html
    queryset = Post.objects.all().order_by('-created')  # Default: Model.objects.all()
    paginate_by = 5  # if pagination is desired
    context_object_name = 'posts_list'  # Default: object_list

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        number_comments = [Comment.objects.filter(post=post).count() for post in context['object_list']]
        context['posts_comments'] = zip(context['object_list'], number_comments)
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'  # Default: <app_label>/<model_name>_form.html

    def get_success_url(self):
        return reverse('users:user_detail', kwargs={'slug': self.object.user})

    def form_valid(self, form):
        if self.request.method == 'POST':
            form.instance.user = self.request.user
            return super(PostCreateView, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.method == 'POST':
            return super(PostCreateView, self).form_invalid(form)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'  # Default: <app_label>/<model_name>_detail.html
    context_object_name = 'post'  # Default: object

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        comments_list = Comment.objects.filter(post=context['object']).order_by('-created')
        number_comments = Comment.objects.filter(post=context['object']).count()
        context['post_comments'] = comments_list
        context['number_comments'] = number_comments
        return context


class PostUptadeView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'  # Default: <app_label>/<model_name>_form.html

    def form_valid(self, form):
        if self.request.method == 'POST':
            return super(PostUptadeView, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.method == 'POST':
            return super(PostUptadeView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('users:user_detail', kwargs={'slug': self.object.user, })


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'  # Default: <app_label>/<model_name>_confirm_delete.html
    context_object_name = 'post'  # Default: object

    def get_success_url(self):
        return reverse('users:user_detail', kwargs={'slug': self.object.user, })


# COMMENTS #

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'posts/comment_form.html'  # Default: <app_label>/<model_name>_form.html

    def form_valid(self, form):
        if self.request.method == 'POST':
            form.instance.user = self.request.user
            #post_obj = get_object_or_404(Post, pk=self.kwargs['pk'])
            post_obj = Post.objects.get(pk=self.kwargs['pk'])
            form.instance.post = post_obj
            return super(CommentCreateView, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.method == 'POST':
            return super(CommentCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('posts:post_detail', kwargs={'pk': self.object.post_id})
        #return reverse('users:user_detail', kwargs={'slug': self.object.user})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'posts/comment_confirm_delete.html'  # Default: <app_label>/<model_name>_confirm_delete.html
    context_object_name = 'comment'  # Default: object

    def get_success_url(self):
        return reverse('posts:post_detail', kwargs={'pk': self.object.post.id, })


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'posts/comment_form.html'  # Default: <app_label>/<model_name>_form.html

    def form_valid(self, form):
        if self.request.method == 'POST':
            return super(CommentUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.method == 'POST':
            return super(CommentUpdateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('posts:post_detail', kwargs={'pk': self.object.post.id, })

