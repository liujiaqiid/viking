# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

def enum(**enums):
    return type(b'Enum', (), enums)

VOTE = enum(DEF=0, ZAN=1, CAI=-1)
VOTE_CHOICE = (
    (VOTE.DEF, "not vote score=0"),
    (VOTE.ZAN, "zan vote score=1"),
    (VOTE.CAI, "cai vote score=-1"),
    )

@python_2_unicode_compatible
class Blog(models.Model):
    id = models.AutoField('blog id', primary_key=True)
    title = models.CharField('blog title', max_length=100)
    subtitle = models.CharField('blog subtitle', max_length=100, null=True, blank=True)
    content = models.CharField('blog content', max_length=2000)
    photo = models.ImageField(upload_to='blogs/%Y/%m/%d', null=True, blank=True)
    # files = models.FileField(upload_to='blogs/%Y/%m/%d', null=True, blank=True)
    created_date = models.DateTimeField('blog created', editable=False, default=timezone.now)

    def was_created_recently(self, days=1):
        """是否是最近创建
        默认为最近1天内创建
        """
        return self.created_date >= timezone.now() - datetime.timedelta(days=days)

    def __str__(self):
        """对象的tostring方法
        """
        return self.title

@python_2_unicode_compatible
class Comment(models.Model):
  id = models.AutoField('comment id', primary_key=True)
  blog = models.ForeignKey(Blog, verbose_name='Blog', null=True, blank=True)
  content = models.CharField('comment content', max_length=200)
  vote = models.IntegerField('vote score', choices=VOTE_CHOICE, default=VOTE.DEF)
  created_date = models.DateTimeField('blog created', editable=False, default=timezone.now)
  def __str__(self):
    return self.content
