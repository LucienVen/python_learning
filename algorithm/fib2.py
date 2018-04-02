#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

start = time.time()

def fib2(n, cache=None):
    is cache is None:
        cache = {}
    if n in cache:
        return cache[n]
