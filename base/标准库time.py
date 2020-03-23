#!/usr/bin/env python3
# -*- coding:utf8 -*-

import time

# 结构化时间，返回只读元组
tr = time.localtime()
print(tr)

# 格式化字符串时间
print(time.strftime('%Y-%m-%d %H:%M:S'))

# 返回时间戳，用于计算
print(time.time())

# 将时间戳转为当前时区的结构化时间
t = time.time() - 1000
print(time.localtime(t))

# 把时间戳转为格式化字符串的本地时间
print(time.ctime(t))

# 将结构化时间转为时间戳
print(time.mktime(tr))

# 字符串时间转为结构化时间
stime = "2017-09-26 12:11:30"
st = time.strptime(stime, '%Y-%m-%d %H:%M:%S')
print(st)


# 进程运行时间/cpu时间
def procedure():
    time.sleep(3)

time1 = time.clock()
procedure()
time2 = time.clock()
print(time2-time1, "seconds process time!")

