#!/usr/bin/env python3
# -*- coding:utf8 -*-


import subprocess

ret = subprocess.run('ls -l', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(ret.stdout.decode())

# 实现交互命令
s = subprocess.Popen('python', stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
s.stdin.write(b"import os\n")
s.stdin.write(b"print(os.name)")
s.stdin.close()

out = s.stdout.read().decode()
s.stdout.close()
print(out)