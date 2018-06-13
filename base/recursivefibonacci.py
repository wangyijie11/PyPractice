#!/usr/bin/env python
# -*- coding:utf-8 -*-


def recur_fibo(n):
    """
    递归函数输出斐波那契数列
    """
    if n <= 1:
        return n
    else:
        return recur_fibo(n-2) + recur_fibo(n-1)


nterms = int(input("需要输出几项："))

if nterms <= 0:
    print("请输入正整数")
else:
    print("斐波那契数列：")
    for i in range(nterms):
        print(recur_fibo(i))
