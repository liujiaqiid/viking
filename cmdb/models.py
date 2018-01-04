#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Iaas Account -> Region -> Zone -> Instance
#
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

def enum(**enums):
  return type(b'Enum', (), enums)

SP_NAME = enum(ALI='aliyun', UCLOUD='ucloud', QING='qingcloud', AWS='aws', JULIYE='juliye')
SP_NAME_CHOICE = (
    (SP_NAME.ALI, _('aliyun')),
    (SP_NAME.UCLOUD, _('ucloud')),
    (SP_NAME.QING, _('qingcloud')),
    (SP_NAME.AWS, _('aws')),
    (SP_NAME.JULIYE, _('juliye')),
    )

CPU_TYPE = enum(
    ENTRY='Intel Xeon CPU',
    GENERAL='Intel Xeon Platinum 8163',
    ENHANCE='Intel Xeon E5-2682v4',
    SUPREME='Intel Xeon Gold 6149',
    )
CPU_TYPE_CHOICE = (
    (CPU_TYPE.ENTRY, _('Entry Level')),
    (CPU_TYPE.GENERAL, _('General Level')),
    (CPU_TYPE.ENHANCE, _('Enhance Level')),
    (CPU_TYPE.SUPREME, _('Supreme Level')),
    )

CPU_NUM = enum(CORE1=1, CORE2=2, CORE4=4, CORE8=8,)
CPU_NUM_CHOICE = (
    (CPU_NUM.CORE1, _('1 Core')),
    (CPU_NUM.CORE2, _('2 Core')),
    (CPU_NUM.CORE4, _('4 Core')),
    (CPU_NUM.CORE8, _('8 Core')),
    )

OS_TYPE = enum(CENTOS='centos', UBUNTU='ubuntu',)
OS_TYPE_CHOICE = (
    (OS_TYPE.CENTOS, _('centos system')),
    (OS_TYPE.UBUNTU, _('ubuntu system')),
    )

DISK_TYPE = enum(GENERAL='general', SSD='ssd',)
DISK_TYPE_CHOICE = (
    (DISK_TYPE.GENERAL, _('general disk')),
    (DISK_TYPE.SSD, _('ssd disk')),
    )

## Iaas Account
@python_2_unicode_compatible
class Iaas(models.Model):
  """ Entity-Iaas
  基础设施服务提供商：ali、aws、qcloud、ucloud、idc
  """

  id = models.AutoField(_('iaas id'), primary_key=True)
  name = models.CharField(_('iaas account name'), max_length=20, unique=True)
  sp = models.CharField(_('iaas provider'), max_length=20, choices=SP_NAME_CHOICE, default=SP_NAME.JULIYE)

  def __str__(self):
    return self.name

## Region
@python_2_unicode_compatible
class Region(models.Model):
  """ Entity-Zone
  服务器地域分组
  """
  id = models.AutoField(_('region id'), primary_key=True)
  iaas = models.ForeignKey(Iaas, verbose_name='IAAS', null=True, blank=True)
  name = models.CharField(_('region name'), max_length=20)
  def __str__(self):
    return self.name

## Zone
@python_2_unicode_compatible
class Zone(models.Model):
  """ Entity-Zone
  服务器管理分组
  """
  id = models.AutoField('zone id', primary_key=True)
  region = models.ForeignKey(Region, verbose_name=_('REGION'), null=True, blank=True)
  name = models.CharField(_('zone name'), max_length=20)
  def __str__(self):
    return self.name

## Instance
@python_2_unicode_compatible
class Instance(models.Model):
  """ Entity-Server
  服务器基本信息
  """
  id = models.AutoField(_('instance id'), primary_key=True)
  name = models.CharField(_('instance name'), max_length=50)
  zone = models.ForeignKey(Zone, verbose_name=_('ZONE'), null=True, blank=True)
  cpu_type = models.CharField(_('cpu type'), max_length=50, choices=CPU_TYPE_CHOICE, default=CPU_TYPE.ENTRY)
  cpu_core = models.IntegerField('cpu core number', choices=CPU_NUM_CHOICE, default=CPU_NUM.CORE1)
  os_type = models.CharField('os type', max_length=50, choices=OS_TYPE_CHOICE, default=OS_TYPE.CENTOS)
  disk_type = models.CharField('disk type', default=DISK_TYPE.GENERAL,choices=DISK_TYPE_CHOICE, max_length=20)
  disk_size = models.IntegerField('disk size', default=40)
  inner_ip = models.CharField('inner ip', max_length=20)
  outer_ip = models.CharField('outer ip', max_length=20, null=True, blank=True)
  created_date = models.DateTimeField('date server created', editable=False, default=timezone.now)
  def __str__(self):
    return self.name
