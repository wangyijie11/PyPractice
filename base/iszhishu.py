#!/usr/bin/env python
# -*- coding:utf-8 -*-

num = int(input("输入数字："))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("{0}不是质数" .format(num))
            break
    else:
        print("{0}是质数" .format(num))
else:
    print("{0}不是质数".format(num))
