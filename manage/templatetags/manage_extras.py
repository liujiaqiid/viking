#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template

register = template.Library()

@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return arg1 + ' / ' + arg2
