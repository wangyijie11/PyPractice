#!/usr/bin/env python3
# -*- coding:utf8 -*-


num = float(input('输入一个数字：'))
if num > 0:
    num_sqrt = num ** 0.5
    print('%0.3f 平方根数为 %0.3f' % (num, num_sqrt))
else:
    print('输入错误数字')


