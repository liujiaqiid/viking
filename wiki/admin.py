# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    """自定义blog管理界面
    """
    # 显示的字段集合，顺序
    # fieldets = []
    # 內联关联的信息
    # inlines = []
    # 列表显示的列信息
    list_display = ('id', 'title', 'subtitle', 'was_created_recently')
    # 列表过滤器
    list_filter = ['created_date']
    # 可搜索字段
    search_fields = ['title']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
