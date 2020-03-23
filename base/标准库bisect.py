#!/usr/bin/env python3
# -*- coding:utf8 -*-


import bisect
import random
x = 200
list1 = [1, 3, 6, 24, 55, 78, 454, 555, 1234, 6900]

# 返回预插入位置，未实际插入
ret = bisect.bisect(list1, x)
print("插入位置：%d" % ret)
print(list1)

# 直接插入列表
ret = bisect.insort(list1, x)
print("插入位置：", ret)
print(list1)


random.seed(1)

print('New  Pos Contents')
print('---  --- --------')
l = []
for i in range(1, 15):
    r = random.randint(1, 100)
    position = bisect.bisect(l, r)
    bisect.insort(l, r)
    print('%3d  %3d' % (r, position), l)