#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

start = time.time()

def fib(n):
    if n==1 or n==0:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

print [fib(n) for n in range(40)]




end = time.time()
print "runtime = {}".format(end - start)
# runtime = 86.8756790161
