#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 二分查找

import time

test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]


def binarySearch(list, targetNum):
    first = 0
    last = len(list)-1
    found = False
    temp = 0
    while first <= last and not found:
        mid = (first+last) / 2
        if list[mid] == targetNum:
            found = True
        else:
            if list[mid] >= targetNum:
                first = mid + 1
            else:
                last = mid - 1
        temp += 1
    return temp

if __name__ == '__main__':
    start = time.time()
    print binarySearch(test_list, 13)
    end = time.time()
    print "running time: {}".format(end - start)
