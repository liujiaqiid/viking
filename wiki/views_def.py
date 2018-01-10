# -*- coding: utf-8 -*-
# 自定义view
#


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse

from .models import Blog, Comment
# Create your views here.

def index(request):
    latest_blog_list = Blog.objects.order_by('-created_date')[:20]
    # output = ",".join([blog.title for blog in latest_blog_list])
    # return HttpResponse("wiki indexes: $s" % output)
    templ = loader.get_template('wiki/index.html')
    context = {
            "latest_blog_list": latest_blog_list
            }
    return HttpResponse(templ.render(context, request))

def details(request, blog_id):
    """获取blog详情
    """
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404("Blog not exists.")
    context = {
            'blog': blog
            }
    # return HttpResponse("You are looking at blog %s details." % blog_id)
    return render(request, 'wiki/blog_detail.html', context)

def comments(request, blog_id):
    """
    """
    blog = get_object_or_404(Blog, id=blog_id)
    comments = Comment.objects.order_by('-created_date')[:20]
    # response = "You are looking at the comments of blog %s"
    # return HttpResponse(response % blog_id)
    context = {
            'comment_list': comments
            }
    return render(request, 'wiki/blog_comment.html', context)

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


