#!/usr/bin/env python
# -*- coding:utf-8 -*-


dic = {"num": "1001", "account": "wangyj", "username": "小何", "age": "20"}
dic["age"] = 22
print(dic)

del dic["age"]
print(dic)

dic["sex"] = "male"
print(dic)

len(dic)
str(dic)
type(dic)