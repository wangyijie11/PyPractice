#!/usr/bin/env python
# -*- coding:utf-8 -*-


li = ["a", "1", "3c", "com", "-23", "1"]
print(li)
print(li[1])
print(li[-1])

li.append("new")
print(li)

li.extend(["one", "two"])
print(li)

li.remove("1")
print(li)

li.pop()
print(li)

li = li + ["21", "22"]
print(li)

li = [elem for elem in li if len(elem) > 2]
print(li)

str = "www.baidu.com"
li = str.split(".")
print(li)

