#!/usr/bin/env python3
# -*- coding:utf8 -*-


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


# 测试内容
print(is_number('wangyijie'))
print(is_number('102'))
print(is_number('-1.02'))
print(is_number('wang2yijie'))