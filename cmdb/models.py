#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

def enum(**enums):
  return type(b'Enum', (), enums)
CPU_TYPE = enum(
    ENTRY='Intel Xeon CPU',
    GENERAL='Intel Xeon Platinum 8163',
    ENHANCE='Intel Xeon E5-2682v4',
    SUPREME='Intel Xeon Gold 6149',
    )
CPU_TYPE_CHOICE = (
    (CPU_TYPE.ENTRY, 'Entry Level'),
    (CPU_TYPE.GENERAL, 'General Level'),
    (CPU_TYPE.ENHANCE, 'Enhance Level'),
    (CPU_TYPE.SUPREME, 'Supreme Level'),
    )

CPU_NUM = enum(CORE1=1, CORE2=2, CORE4=4, CORE8=8,)
CPU_NUM_CHOICE = (
    (CPU_NUM.CORE1, '1 Core'),
    (CPU_NUM.CORE2, '2 Core'),
    (CPU_NUM.CORE4, '4 Core'),
    (CPU_NUM.CORE8, '8 Core'),
    )

OS_TYPE = enum(CENTOS='centos', UBUNTU='ubuntu',)
OS_TYPE_CHOICE = (
    (OS_TYPE.CENTOS, 'centos system'),
    (OS_TYPE.UBUNTU, 'ubuntu system'),
    )
DISK_TYPE = enum(GENERAL='general', SSD='ssd',)
DISK_TYPE_CHOICE = (
    (DISK_TYPE.GENERAL, 'general disk'),
    (DISK_TYPE.SSD, 'ssd disk'),
    )

## Iaas
@python_2_unicode_compatible
class Iaas(models.Model):
  """ Entity-Iaas
  基础设施服务提供商：ali、aws、qcloud、ucloud、idc
  """

  id = models.AutoField('iaas id', primary_key=True)
  name = models.CharField('iaas name', max_length=20)

  def __str__(self):
    return self.name

## Zone
@python_2_unicode_compatible
class Zone(models.Model):
  """ Entity-Zone
  服务器管理分组
  """
  id = models.AutoField('zone id', primary_key=True)
  #FIXME:
  iaas = models.ForeignKey(Iaas, verbose_name='IAAS', null=True, blank=True)
  name = models.CharField('zone name', max_length=20)
  def __str__(self):
    return self.name

## Server
@python_2_unicode_compatible
class Server(models.Model):
  """ Entity-Server
  服务器基本信息
  """
  id = models.AutoField('server id', primary_key=True)
  name = models.CharField('server name', max_length=50)
  zone = models.ForeignKey(Zone, verbose_name='ZONE', null=True, blank=True)
  cpu_type = models.CharField('cpu type', max_length=50, choices=CPU_TYPE_CHOICE, default=CPU_TYPE.ENTRY)
  cpu_core = models.IntegerField('cpu core number', choices=CPU_NUM_CHOICE, default=CPU_NUM.CORE1)
  os_type = models.CharField('os type', max_length=50, choices=OS_TYPE_CHOICE, default=OS_TYPE.CENTOS)
  disk_type = models.CharField('disk type', default=DISK_TYPE.GENERAL,choices=DISK_TYPE_CHOICE, max_length=20)
  disk_size = models.IntegerField('disk size', default=40)
  inner_ip = models.CharField('inner ip', max_length=20)
  outer_ip = models.CharField('outer ip', max_length=20, null=True, blank=True)
  created_date = models.DateTimeField('date server created', editable=False, default=timezone.now)
  def __str__(self):
    return self.name
