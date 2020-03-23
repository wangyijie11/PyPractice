#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
# json模块不支持bytes类型，需要先转str
print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
print(json.loads('["foo", {"bar": ["baz", null, 1.0, 2]}]'))

dic = {'user': 'ZhangSan', 'type': 'work',
       'team': [{'city': 'BeiJing', 'num': 3}, {'city': 'GuangZhou', 'num': 3}, {'city': 'ShangHai', 'num': 3}]}
f = json.dump(dic, open('example_json', 'w'))
obj = json.load(open('example_json'))
print(obj)