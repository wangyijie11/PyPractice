#!/usr/bin/env python
# -*- coding:utf-8 -*-


import threading
import time

number = 0
lock = threading.Lock()


def plus(lk):
    global number
    with lk:  # with语句，实现锁管理，自动加锁、解锁
        for _ in range(100000):
            number += 1
        print("子线程%s运算结束后，number = %s" % (threading.current_thread().getName(), number))


if __name__ == '__main__':
    for i in range(2):  # 启动2个子线程
        t = threading.Thread(target=plus, args=(lock,))   # 把锁当作参数传给plus函数
        t.start()
    time.sleep(2)
    print("主线程执行完毕后，number = ", number)