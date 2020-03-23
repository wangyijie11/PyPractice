#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Process
from multiprocessing import Array
from multiprocessing import RLock, Lock, Event, Condition, Semaphore
import time


def func(i, lis, lc):
    with lc:
        lis[0] = lis[0] - 1
        time.sleep(1)
        print('say hi', lis[0])


if __name__ == '__main__':
    array = Array('i', 1)
    array[0] = 10
    lock = RLock()
    for i in range(10):
        p = Process(target=func, args=(i, array, lock))
        p.start()
