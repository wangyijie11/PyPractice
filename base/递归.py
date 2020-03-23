#!/usr/bin/env python3
# -*- coding:utf8 -*-


def sum_number(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

print(sum_number(100))

def sum_number_dg(n):
    if n <= 0:
        return 0
    return n + sum_number_dg(n-1)

print(sum_number_dg(100))