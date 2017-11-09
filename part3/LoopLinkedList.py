#!/usr/bin/env python
# -*- coding:utf-8 -*-

from SingleLinkedList import LNode, LinkedListUnderflow

# 循环单链表的实现
class LCList:
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    # 表头插入
    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    # 表尾插入
    def append(self, elem):
        # p = LNode(elem, self._rear.next)
        # self._rear.next = p
        # self._rear = p
        self.prepend(elem)
        self._rear.next = self._rear

    # 前端弹出
    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow("in pop of CLList")
        
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        
        return p.elem

    # 输出表元素
    def printAll(self):
        if self.is_empty():
            return
        
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p.next



