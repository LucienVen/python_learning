#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 单链表类的实现

# 定义简单的节点类
class LNode:
    def __init__(self, elem, next_=None):
        # elem 表元素域
        # next 下一结点链接域（next_避免与标准函数next重名）
        self.elem = elem
        self.next = next_


# 自定义异常
class LinkedListUnderflow(ValueError):
    pass


# LList类的定义、初始化函数与简单操作
class LList:
    def __init__(self):
        # 初始化定义创建的是一个空表
        self._head = None

    def is_empty(self):
        return self._head is None

    # 在表首插入元素elem
    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    # pop删除表头结点并返回这个结点里的元素
    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e

    # 在表尾插入元素
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return 
        # 找到链表最后一个结点
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    # 删除并返回表的最后元素
    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        
        p = self._head
        # 如果表中只有一个元素
        if p.next is None:
            e = p.elem
            self._head = None
            return e

        while p.next.next is not None:
            p = p.next
         
        e = p.next.elem
        p.next = None
        return e




# 对LNode简单使用
# def main():
#     llist1 = LNode(1)
#     p = llist1
#     for i in range(2,11):
#         p.next = LNode(i)
#         p = p.next

#     p = llist1
#     while p is not None:
#         print(p.elem)
#         p = p.next


# if __name__ == '__main__':
#     main()