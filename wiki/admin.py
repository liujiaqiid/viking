# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Blog, Comment

class TitleFilter(admin.SimpleListFilter): #, latest_10_topic_list):
    """ 标题过滤器
    """
    title = _('blog title')
    parameter_name = 'title'

    def lookups(self, request, model_admin):
        """只显示前5个title作为过滤词
        """
        filters = ()
        result = model_admin.get_queryset(request)[:5]
        # Build tulples
        for res in result:
            # print("res %s : %s" % (res.title, type(res)))
            filters = filters + ((res.title, res.title), )
        return filters
        # return super(TitleFilter, self).lookups(request, model_admin)
        # return ((1, "111"),(2, "222"))

    def queryset(self, request, queryset):
        """ 过滤方式
        """
        title = self.value()
        print("query set ... %s" % title)
        if title:
            # return queryset.filter(title__contains = title)[:10]
            return queryset.filter(title__contains = title) #[:10]
        else:
            return queryset.all() # [:10]

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
    list_filter = ['created_date', TitleFilter]
    # 可搜索字段
    search_fields = ['title']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
