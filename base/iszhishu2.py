#!/usr/bin/env python
# -*- coding:utf-8 -*-

lower = int(input("输入最小区间："))
upper = int(input("输入最大区间："))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
