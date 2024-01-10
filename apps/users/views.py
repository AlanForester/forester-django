# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from .models import User
from .forms import UserEditForm

from ..posts.models import Post, Comment


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/user_detail.html'  # Default: <app_label>/<model_name>_detail.html
    slug_field = 'username'
    context_object_name = 'user'  # Default: object

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        posts_list = Post.objects.filter(user=context['object']).order_by('-created')

        page = self.request.GET.get('page', 1)
        paginator = Paginator(posts_list, 3)
        posts = paginator.page(page)

        number_comments = [Comment.objects.filter(post=post).count() for post in posts]

        context['posts_user_comments'] = zip(posts, number_comments)
        context['page_obj'] = posts

        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    slug_field = 'username'
    template_name = 'users/user_form.html'  # Default: <app_label>/<model_name>_form.html

    def form_valid(self, form):
        if self.request.method == 'POST':
            return super(UserUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.method == 'POST':
            return super(UserUpdateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('users:user_detail', kwargs={'slug': self.object.username})


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    slug_field = 'username'
    template_name = 'users/user_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('homepage')
