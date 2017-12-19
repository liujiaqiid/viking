#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'wikis'

urlpatterns = [
        # ex: /wiki/
        url(r'^$', views.index, name='index'),
        url(r'^(?P<blog_id>[0-9]+)/$', views.details, name='details'),
        url(r'^(?P<blog_id>[0-9]+)/comments/$', views.comments, name='comments'),
        url(r'^(?P<blog_id>[0-9]+)/votes/$', views.votes, name='votes'),
        ]
