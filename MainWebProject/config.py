#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2019/5/6 9:02
# software: PyCharm


import configparser
import os
def getConfig(section, key):
    config = configparser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '/settins.conf'
    config.read(path)
    return config.get(section, key)