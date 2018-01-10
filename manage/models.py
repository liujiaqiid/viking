# -*- coding: utf-8 -*-


from django.db import models

class Userinfo(models.Model):
    name = models.CharField(unique=True, max_length=128, verbose_name='用户名')
    password = models.CharField(max_length=128, verbose_name='用户密码')
    email = models.EmailField(verbose_name='邮箱')
