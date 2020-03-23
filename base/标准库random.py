#!/usr/bin/env python3
# -*- coding:utf8 -*-


import random

# 生成一个包含大写字母A-Z和数字0-9的随机4位验证码的程序
checkcode = ''
for i in range(4):
    current = random.randrange(0,4)
    if current != i:
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print(checkcode)