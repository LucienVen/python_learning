#!/usr/bin/env python
# -*- coding:utf-8 -*-

#  顺序查找
import time

test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]

def sequentialSearch(list, targetNum):
    temp = 0
    found = False

    while(temp < len(list) and not found):
        for i in test_list:
            if(i == targetNum):
                found = True
            else:
                temp += 1
        return temp



if __name__ == '__main__':
    start = time.time()
    print sequentialSearch(test_list,1)
    end = time.time()
    print "running time: {}".format(end - start)
