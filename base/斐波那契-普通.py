#!/usr/bin/env python
# -*- coding:utf-8 -*-

nterms = int(input("输入需要几项："))

n1 = 0
n2 = 1
count = 2

if nterms == 0:
    print("请输入一个正整数")
elif nterms == 1:
    print("fibonacci:")
    print(n1)
else:
    print("fibonacci:")
    print(n1, ",", n2, end=",")
    while count < nterms:
        nth = n1 + n2
        print(nth, end=",")
        n1 = n2
        n2 = nth
        count += 1
