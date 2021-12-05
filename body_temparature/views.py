from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.views import generic
from django.urls import reverse_lazy
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserList(generic.ListView):
    """ユーザー一覧ページ"""
    model = User
    template_name = 'body_temparature/top.html'

class UserDetail(generic.ListView):
    """ユーザーごとのlog"""
    model = models.Log
    template_name = 'body_temparature/user_detail.html'
    ordering = '-day'

    def get_queryset(self):
        queryset = super().get_queryset()
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return queryset.filter(user=user)

    def get_context_data(self):
        context = super().get_context_data()
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        context['user'] = user
        return context