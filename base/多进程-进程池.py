#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Pool
import time

def func(args):
    time.sleep(1)
    print("正在执行进程", args)

if __name__ == '__main__':
    # 创建容量为5的进程池
    p = Pool(5)

    for i in range(30):
        p.apply_async(func=func, args=(i,))

    p.close()
    # time.sleep(2)
    # p.terminate()     # 立刻关闭进程池
    p.join()