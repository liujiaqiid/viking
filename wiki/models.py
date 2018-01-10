# -*- coding: utf-8 -*-


from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

import datetime

# Create your models here.

def enum(**enums):
    return type('Enum', (), enums)

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
        return timezone.now() >= self.created_date >= timezone.now() - datetime.timedelta(days=days)

    def __str__(self):
        """对象的tostring方法
        """
        return self.title

@python_2_unicode_compatible
class Comment(models.Model):

    id = models.AutoField('comment id', primary_key=True)
    blog = models.ForeignKey(Blog, on_delete=True, verbose_name='Blog', null=True, blank=True)
    content = models.CharField('comment content', max_length=200)
    vote = models.IntegerField('vote score', choices=VOTE_CHOICE, default=VOTE.DEF)
    created_date = models.DateTimeField('blog created', editable=False, default=timezone.now)

    def is_valid_vote(self):
        # print("vote : %s" % self.vote)
        return self.vote in (VOTE.DEF, VOTE.ZAN, VOTE.CAI)

    def save(self, *args, **kwargs):
        if not self.is_valid_vote():
            print("not valid vote!! ")
            raise ValueError("The vote value isn't allowed")
        else:
            super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return self.content
