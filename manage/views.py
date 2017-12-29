# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import hashlib
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from cmdb.models import Server

def _hash_password(password):
    '''md5加密
    :param password:
    :return: 加密后的字符串
    '''
    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()

def _is_user_exist(username):
    '''用户是否存在
    :param username:
    :return: bool
    '''
    if Userinfo.objects.filter(name = username):
        return True
    else:
        return False

def _login_check(func):
    '''是否登陆
    '''
    def check(req, *a, **k):
        #TODO: 加密验证
        name = req.COOKIES.get("name")
        if not name:
            return HttpResponseRedirect('/manage/login')
        return func(req, *a, **k)
    return check

@_login_check
def index(req):
    '''首页
    '''
    username = req.COOKIES.get('name','')
    return render(req, 'manage/index.html', locals())

def register(req):
    '''注册页面
    '''
    if req.method == 'POST' and req.POST:
        username = req.POST['username']
        if _is_user_exist(username):
            warning = '用户名已存在，请重新选一个独特的用户名'
            return render(req, 'manage/register.html', locals())
        user = Userinfo()
        user.name = username
        user.password = _hash_password(req.POST['password'])
        user.email = req.POST['email']
        user.save()
        return HttpResponseRedirect('/manage/login')
    else:
        return render(req, 'manage/register.html')

def login(req):
    if req.method == 'POST' and req.POST:
        username = req.POST['username']
        password = req.POST['password']
        password = _hash_password(password)

        if (_is_user_exist(username)):
            dbpassword = Userinfo.objects.get(name=username).password
            if dbpassword == password:
                response = HttpResponseRedirect('/manage/index')
                response.set_cookie('name', username, max_age=3600)
                req.session['name'] = username
                return response
            else:
                error = '用户名或密码错误，请重新输入'
                return render(req, 'manage/login.html', locals())
        else:
            error = '用户名或密码错误，请重新输入'
            return render(req, 'manage/login.html', locals())
    else:
        return render(req, 'manage/login.html', locals())

@_login_check
def hostlist(req):#主机列表信息
    username = req.COOKIES.get('name', '')
    server_list = Server.objects.all()
    return render(req, 'manage/hostlist.html', locals())
