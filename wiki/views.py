# -*- coding: utf-8 -*-
# 通用view模版
#
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Blog, Comment
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'wiki/index.html'
    context_object_name = 'latest_blog_list'
    def get_queryset(self):
        """Return the last five published questions."""
        return Blog.objects.filter(
                created_date__lte=timezone.now()
                ).order_by('-created_date')[:20]

class DetailView(generic.DetailView):
    model = Blog
    template_name = 'wiki/blog_detail.html'
    # context_object_name = 'the_blog'
    def get_queryset(self):
        """
        """
        return Blog.objects.filter(created_date__lte=timezone.now())

class CommentsView(generic.ListView):
    model = Comment
    template_name = 'wiki/blog_comment.html'
    def get_queryset(self):
        """Return the last five published questions."""
        return Comment.objects.order_by('-created_date')[:5]

def comment(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    content = request.POST['content']
    vote = int(request.POST['vote'])
    if not content:
        return render(request, 'wiki/blog_detail.html',
                {
                    'blog': blog,
                    'error_message': '非法评论'
                    })
    else:
        try:
            blog.comment_set.create(content=content, vote=vote)
        except ValueError as err:
            return render(request, 'wiki/blog_detail.html',
                    {
                        'blog': blog,
                        'error_message': '非法评分'
                        })
        return HttpResponseRedirect(reverse('wiki:comments', args=(blog.id,)))
