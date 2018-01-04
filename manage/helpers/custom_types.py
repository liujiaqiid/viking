#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 自定义数据类型
#

def enum(**enums):
    """枚举类型
    """
    return type(b'Enum', (), enums)
