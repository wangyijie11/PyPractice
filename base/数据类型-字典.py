#!/usr/bin/env python
# -*- coding:utf-8 -*-

dic = {'name': 'wang', 'age': '18'}
dic2 = {'addr': '华星路'}
print(dic.get('name'))
print(dic.items())
print(dic.keys())
print(dic.values())
print(dic.popitem())
print(dic.pop('name'))
print(dic.setdefault('name','wangyj'))
print(dic.update(dic2))
print(dic.copy())
print(dic.clear())
print(dic.fromkeys('1 2 3', '你 好 啊'))