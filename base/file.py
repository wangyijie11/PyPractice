#!/usr/bin/env python3
# -*- coding:utf8 -*-


def file_read():
    f = open("/Users/wangyijie/PycharmProjects/pypractice/base/ceshi", "rb")
    for line in f:
        print(line, end='')
    point = f.tell()
    print(point)
    f.seek(4, 0)
    print(f.read(2))
    f.close()


def file_write():
    f = open("/Users/wangyijie/PycharmProjects/pypractice/base/ceshi", "rb+")
    f.write(b"asdfghjkl\n1234567890\n")
    point = f.tell()
    print(point)
    f.close()


file_read()
