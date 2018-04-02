#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 1-n 阶乘


def factorial(n):
    temp = 1
    for i in range(1,n+1):
        temp = temp * i
    print("{}! = {}".format(n, temp))

factorial(4)


# 打印九九乘法表
def MultiplicationTable():
    for i in range(1,10):
        print('')
        for j in range(1, 10):
            if j > i:
                break
            print("{}x{}={}".format(i, j, i*j), end=' ')

MultiplicationTable()

