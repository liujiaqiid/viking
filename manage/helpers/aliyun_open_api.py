#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 阿里云开放API工具
#
from __future__ import unicode_literals
import json
from aliyunsdkcore.client import AcsClient
# from aliyunsdkcore.request import CommonRequest
import aliyunsdkcore.request as AliReq
from aliyunsdkecs.request.v20140526 import DescribeRegionsRequest
from aliyunsdkecs.request.v20140526 import DescribeZonesRequest
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import DescribeInstanceStatusRequest
from aliyunsdkecs.request.v20140526 import DescribeInstancesFullStatusRequest

import custom_types as _types

API_DEFAULT_VERSION = '2014-05-26'
API_DEFAULT_DOMAIN = 'ecs.aliyuncs.com'
API_LIST = _types.enum( # API 列表
        DescribeRegions='DescribeRegions', # 查看region列表
        DescribeZones='DescribeZones', # 查看zones列表
        DescribeInstances='DescribeInstances', # 查看机器列表
        DescribeInstanceStatus='DescribeInstanceStatus', # 查看机器状态列表
        )
PAGE_NUM = '1'
PAGE_SIZE = '20'

def _load_default_config():
    print("load config")
    with open('manage/config/_aliyun_config.json') as fp:
        config = json.loads(fp.read())
    return config

DEFAULT_CONFIG = _load_default_config()

def _get_config(region=DEFAULT_CONFIG['region_id']):
    config = DEFAULT_CONFIG
    config['region_id'] = region
    return config

# 设置全局默认协议为https
AliReq.set_default_protocol_type("https")

def _start_client(config):
    client = AcsClient(
            config['access_key_id'],
            config['access_key_secret'],
            config['region_id'])
    return client

def _do_action(config, request):
    try:
        client = _start_client(config)
        response = client.do_action_with_exception(request)
    except Exception as e:
        print('API Exception: %s' % e)
        return ''
    return response

def common_request(action=API_LIST.DescribeRegions):
    """通用API请求
    """
    # 创建 request，并设置参数
    request = AliReq.CommonRequest()
    #request.set_protocol_type("https") # 默认为http请求
    request.set_domain(API_DEFAULT_DOMAIN)
    request.set_version(API_DEFAULT_VERSION)
    request.set_action_name(action)
    request.add_query_param('PageNumber', PAGE_NUM)
    request.add_query_param('PageSize', PAGE_SIZE)
    # 发起 API 请求并返回数据
    return _do_action(_get_config(), request)

def ecs_region_list_request():
    """ECS封装API-获取地域列表
    - Data['Regions']
        -
        - Data['Regions']['Region'][0]['LocalName']
    - Data['RequestId']
    """
    # 创建 request，并设置参数
    request = DescribeRegionsRequest.DescribeRegionsRequest()
    # 发起 API 请求并返回数据
    return _do_action(_get_config(), request)

def ecs_zone_list_request(region=DEFAULT_CONFIG['region_id']):
    """ECS封装API-获取分组列表
    - Date['Zones']
        - Data['Zones']['Zone'][0]['ZoneId']
        - Data['Zones']['Zone'][0]['LocalName']
    - Data['RequestId']
    """
    # 创建 request，并设置参数
    request = DescribeZonesRequest.DescribeZonesRequest()
    # 发起 API 请求并返回数据
    return _do_action(_get_config(region), request)


def ecs_instance_list_request(zone_id=''):
    """ECS封装API-获取分组列表
    """
    # 创建 request，并设置参数
    request = DescribeInstancesRequest.DescribeInstancesRequest()
    request.set_PageSize(PAGE_SIZE)
    request.set_PageNumber(PAGE_NUM)
    if zone_id:
        request.set_ZoneId(zone_id)
    # 发起 API 请求并返回数据
    return _do_action(_get_config(region), request)
