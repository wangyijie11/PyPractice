#!/usr/bin/env python3
# -*- coding:utf8 -*-


import hashlib
# 支持的加密类型
print(hashlib.algorithms_guaranteed)
s = 'password' + 'salt'

md5 = hashlib.md5()
md5.update(s.encode())
print(md5.hexdigest())

sh256 = hashlib.sha256()
sh256.update(s.encode())
print(sh256.hexdigest())