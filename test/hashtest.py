#!/usr/bin/python3
# author:zxing
# -*- coding:utf-8 -*-
# @time     : 3:57 下午
# @site     :
# @File     :hashtest.py
# @software :PyCharm
import hashlib

passwd = 'ZXSSJDY'
md5 = hashlib.md5()
md5.update(passwd.encode('utf-8'))
print(md5.hexdigest())
