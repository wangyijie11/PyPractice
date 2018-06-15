#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 基类定义
class people:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s今年%d岁" %(self.name, self.age))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print("%s今年%d岁，读%d年级" %(self.name, self.age, self.grade))


# 另一个类，多重继承的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self, n, t):
        self.name = n
        self.topic = t
    def speak(self):
        print("%s是一个演说家，演讲的主题是%s" %(self.name, self.topic))


# 多重继承
class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)

p = sample('小马', 18, 45, 6, '人工智能')
p.speak()