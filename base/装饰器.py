#!/usr/bin/env python3
# -*- coding:utf8 -*-


def outer(func):
    def inner(username):
        print("认证成功")
        # 调用f1原先的code
        result = func(username)
        print("日志添加成功")
        return result
    return inner

@outer
def f1(name):
    print("%s 业务部门1数据接口。。。" % name)

f1('wangyijie')