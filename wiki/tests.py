# -*- coding: utf-8 -*-

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

import datetime

from .models import Blog, Comment

# Model Test - Functional Test
class BlogModelTests(TestCase):

    def test_was_published_recently_with_future_blog(self):
        """
        创建时间大于当前时间（未来）的博客不属于最近创建的
        即 was_published_recently 方法返回false
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_blog = Blog(created_date=time)
        self.assertIs(future_blog.was_created_recently(), False)

    def test_was_published_recently_with_old_blog(self):
        """
        创建时间早于1天前为 非最近创建
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_blog = Blog(created_date=time)
        self.assertIs(old_blog.was_created_recently(), False)

    def test_was_published_recently_with_recent_blog(self):
        """
        创建时间在1天以内的 为 最近创建
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_blog = Blog(created_date=time)
        self.assertIs(recent_blog.was_created_recently(), True)

def create_blog(title, content, days):
    """
    创建blog
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Blog.objects.create(title=title, content=content, created_date=time)

#
class BlogIndexViewTests(TestCase):

    def test_demo(self):
        self.assertIs(1==1, True)

    def test_no_blog(self):
        """
        """
        response = self.client.get(reverse('wiki:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No blog are available")
        self.assertQuerysetEqual(response.context['latest_blog_list'], [])

    def test_past_blog(self):
        """
        """
        create_blog(title='test', content="test blog", days=-10)
        response = self.client.get(reverse('wiki:index'))
        self.assertQuerysetEqual(
                response.context['latest_blog_list'],
                ['<Blog: test>']
                )

    def test_future_blog(self):
        """
        """
        create_blog(title="test future", content="test blog", days=10)
        response = self.client.get(reverse('wiki:index'))
        self.assertContains(response, "No blog are available")
        self.assertQuerysetEqual(response.context['latest_blog_list'], [])

    def test_future_past_blog(self):
        """
        """
        create_blog(title="test future", content="test blog", days=10)
        create_blog(title="test past", content="test blog", days=-10)
        response = self.client.get(reverse('wiki:index'))
        self.assertQuerysetEqual(
                response.context['latest_blog_list'],
                ['<Blog: test past>']
                )

    def test_multi_past_blog(self):
        """
        """
        create_blog(title="test past 1", content="test blog", days=-10)
        create_blog(title="test past 2", content="test blog", days=-10)
        create_blog(title="test past 3", content="test blog", days=-10)
        response = self.client.get(reverse('wiki:index'))
        self.assertQuerysetEqual(
                response.context['latest_blog_list'],
                ['<Blog: test past 3>', '<Blog: test past 2>', '<Blog: test past 1>']
                )

class BlogDetailViewTest(TestCase):
    """
    """
    def test_future_detail(self):
        """
        """
        future_blog = create_blog(title='test future', content='test blog', days=10)
        url = reverse('wiki:details', args=(future_blog.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_detail(self):
        """
        """
        past_blog = create_blog(title='test future', content='test blog', days=-10)
        url = reverse('wiki:details', args=(past_blog.id,))
        response = self.client.get(url)
        self.assertContains(response, past_blog.title)
