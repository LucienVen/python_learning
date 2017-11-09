#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from SingleLinkedList import LNode, LList, LinkedListUnderflow

# 继承和扩充定义新链表类
# 带尾结点的单链表类

class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        self._rear = None

    # 覆盖prepend方法，表首插入元素
    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    # append，表尾插入元素
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    # 弹出末元素的操作pop_last
    def pop_last(self):
        # 判断是否为空表
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        # 如果表只有一个元素
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        # 直到p.next是最后结点
        # 因为链表没有向前的结点选项，只能向后查找
        # if(return e = self._rear), but _rear will can't define, so....use traverse
        while p.next.next is not None:
            p = p.next

        e = p.next.elem
        self._rear = p
        return e
