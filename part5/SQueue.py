#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 栈的实现
class QueueUnderflow(ValueError):
    pass

class SQueue():
    def __init__(self, init__len=8):
        # 存储区长度
        self._len = init__len
        # 元素存储
        self._elems = [0] * init__len
        # 表头元素下标
        self._head = 0
        # 元素个数
        self._num = 0
    
    # 判断队列是否为空
    def is_empty(self):
        return self._num == 0

    # 取队列首元素
    def peek(self):
        if self._num == 0:
            raise QueueUnderflow
        return self._elems[self._head]
    
    # 出队
    def dequeue(self):
        if self._num == 0:
            raise QueueUnderflow
        
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e

    # 入队
    def enqueue(self, e):
        if self._num == self._num:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = e
        self._num += 1
        

    # 若队列以满，拓展队列长度的方法
    def __extend(self):
        old_len = self._len
        self._len *= 2

        new_elems = [0] * self._len
        # 把就队列里的值，重新入新队列
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head+i) % old_len]
        
        self._elems, self._head = new_elems, 0