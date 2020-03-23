#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import queue
import threading

# 生成一个容量为10的队列
q = queue.Queue(10)

def productor(i):
    # 厨子每2秒做一个包子
    while True:
        q.put("厨子 %s 做的包子" % i)
        time.sleep(2)

def consumer(j):
    # 顾客每1秒吃一个包子
    while True:
        print("顾客 %s 吃了一个 %s" % (j, q.get()))
        time.sleep(1)

# 实例化3个生产者
for i in range(3):
    t = threading.Thread(target=productor, args=(i,))
    t.start()

# 实例化5个消费者
for j in range(5):
    v = threading.Thread(target=consumer, args=(j,))
    v.start()
