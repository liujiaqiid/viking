#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'wiki'

urlpatterns = [
        # ex: /wiki/
       # url(r'^$', views.index, name='index'),
       # url(r'^(?P<blog_id>[0-9]+)/$', views.details, name='details'),
       # url(r'^(?P<blog_id>[0-9]+)/comments/$', views.comments, name='comments'),
       # url(r'^(?P<blog_id>[0-9]+)/comment/$', views.comment, name='comment'),

         url(r'^$', views.IndexView.as_view(), name='index'),
         url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
         url(r'^(?P<pk>[0-9]+)/comments/$', views.CommentsView.as_view(), name='comments'),
         url(r'^(?P<blog_id>[0-9]+)/comment/$', views.comment, name='comment'),
        ]
