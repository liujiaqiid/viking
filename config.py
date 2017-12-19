#!/usr/bin/env python
# -*- coding: utf-8 -*-

import aumbry

class UserConfig(aumbry.JsonConfig):
  __mapping__ = {
    "uuid": ["uuid", str]
  }

class ServerConfig(aumbry.JsonConfig):
  __mapping__ = {
    "master": ["master", str],
    "slave": ["slave", str]
  }

class RpcConfig(aumbry.JsonConfig):
  __mapping__ = {
    "version": ["version", int],
    "user": ["user", UserConfig],
    "server": ["server", ServerConfig],
    "port": ["port", int],
    "auth_ips": ["auth_ips",  list]
  }

_options = {
  'CONFIG_FILE_PATH': './.secret.json',
}

CONFIG = aumbry.load(aumbry.FILE, RpcConfig, _options)
# print("load app config, version: %s " % CONFIG.version)
