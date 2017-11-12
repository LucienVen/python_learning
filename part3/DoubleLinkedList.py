#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 双链表的实现

from SingleLinkedList import LNode, LinkedListUnderflow

# 带尾结点的单链表类
from withTailNodeLinkedList import LList1

class DLNode(LNode):
    def __init__(self, elem, prev=None, next_=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev

class DLList(LList1):
    def __init__(self):
        LList1.__init__(self)   # _head, _rear

    # 表头插入元素
    def prepend(self, elem):
        p = DLNode(elem, None, self._head)  # p.
        if self._head is None:
            self._head = p
        else:
            p.next.prev = p
        self._head = p

    # 表尾插入元素
    def append(self, elem):
        p = DLNode(elem, self._rear, None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop of DLList")
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last of DLList")
        e = self._rear.elem
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e