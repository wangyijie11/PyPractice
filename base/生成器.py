#!/usr/bin/env python3
# -*- coding:utf8 -*-

# fibonacci
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1

fib = fibonacci(10)
print(type(fib))
for i in fib:
    print(i, end=" ")