#!/usr/bin/env python3
# -*- coding:utf8 -*-

li = [x * x for x in range(1, 10)]
print(li)

li2 = [x * x for x in range(1, 10) if x % 2 == 0]
print(li2)

li3 = [a + b for a in '123' for b in 'abc']
print(li3)