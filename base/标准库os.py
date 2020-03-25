#!/usr/bin/env python3
# -*- coding:utf8 -*-


import os
import time, datetime

# print('name: %s\nenviron: %s\nsep: %s\naltsep: %s\nextsep: %s\npathsep: %s\nlinesep: %s\ndevnull: %s\ndefpath: %s\n'
#      %(os.name, os.environ, os.sep, os.altsep, os.extsep, os.pathsep, os.linesep, os.devnull, os.defpath))

print('当前工作路径：%s' % os.getcwd())
print(os.curdir)
print((os.pardir))
# os.makedirs('./dir1/dir2')
# os.chdir('./dir1/dir2')
# os.removedir('./dir1/dir2')
dirs = os.listdir('./')
print(dirs)
# os.rename('99.py','九九乘法表.py')

print(os.stat('ceshi'))
# os.remove('ceshi')

print(os.path.abspath('.'))
print(os.path.dirname('/Users/wangyijie/PycharmProjects/pypractice/base/ceshi'))
print(os.path.basename('/Users/wangyijie/PycharmProjects/pypractice/base/ceshi'))
print(os.path.exists('/Users/wangyijie/PycharmProjects/pypractice/base'))
print(os.path.isabs('/Users/wangyijie/PycharmProjects/pypractice/base'))
print(os.path.isfile('/Users/wangyijie/PycharmProjects/pypractice/base'))
print(os.path.isdir('/Users/wangyijie/PycharmProjects/pypractice/base'))
print(os.path.join('/Users/wangyijie/', 'ycharmProjects/pypractice/base'))
print(os.path.getsize('/Users/wangyijie/PycharmProjects/pypractice/base/ceshi'))
print(os.path.getmtime('/Users/wangyijie/PycharmProjects/pypractice/base/ceshi'))
print(os.path.getatime('/Users/wangyijie/PycharmProjects/pypractice/base/ceshi'))
