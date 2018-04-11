#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^iaaslist/', views.iaaslist, name='iaasList'),
    url(r'^regionlist/', views.regionlist, name='regionList'),
    url(r'^zonelist/', views.zonelist, name='zoneList'),
    url(r'^instancelist/', views.instancelist, name='instanceList'),
    url(r'^autodeploy/deploy/', views.auto_deploy_repo, name='auto_deploy'),
    url(r'^autodeploy/', views.auto_deploy_index, name='auto_deploy_index'),
    ]
