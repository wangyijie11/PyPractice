#!/usr/bin/env python3
# -*- coding:utf8 -*-


from datetime import datetime, timedelta
import time

print(datetime.today())
print(datetime.now())
print(datetime.fromtimestamp(time.time()))
print(datetime.strptime('2017/05/04 10:23', '%Y/%m/%d %H:%M'))


dt = datetime.now()
# 返回的是一个datetime 对象
print(type(dt))
print(dt.strftime('%Y/%m/%d %H:%M:%S.%f'))

# 3小时前
dlt = dt + timedelta(hours=-3)
# 3小时30秒后
dlt2 = dt + timedelta(hours=3, seconds=30)
print(dlt)
print(dlt2)
print((dlt2 - dlt).seconds)

