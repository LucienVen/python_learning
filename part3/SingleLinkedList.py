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
            # print(e)
            return e

        while p.next.next is not None:
            p = p.next

        e = p.next.elem
        p.next = None
        # print(e)
        return e

    # 找到满足给定条件的表元素
    #  ?????? 怎么使用？？？？
    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    # 返回被操作的表的情况
    def printAll(self):
        p = self._head
        temp = 0
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
            temp += 1
        print('')
        print("length:{}".format(temp))

    # 表的遍历
    def for_each(self, proc):   # proc => eg:print
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next

    # 为LList类定义对象的一个迭代器
    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    # 筛选生成器
    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next


    # 插入排序，移动表中元素
    def sort1(self):
        if self._head is None:
            return
        crt = self._head.next   # 从首结点之后开始处理
        while crt is not None:
            x = crt.elem
            p = self._head
            # 跳过小元素
            while p is not crt and p.elem <= x:
                p = p.next
            while p is not crt:
                y = p.elem
                p.elem = x
                x = y
                p = p.next
            
            crt.elem = x
            crt = crt.next

    # 插入排序，调整链接的方式
    def sort(self):
        p = self._head
        if p is None or p.next is None:
            return
        
        rem = p.next
        p.next = None

        while rem is not None:
            p = self._head
            q = None

            while p is not None and p.elem <= rem.elem:
                q = p
                p = p.next
            
            if q is None:
                self._head = rem
            else:
                q.next = rem
            
            q = rem
            rem = rem.next
            q.next = p


    # 删除倒数第N个元素
    # def removeNthFromEnd(self, n):
    #     if self._head is None:
    #         raise LinkedListUnderflow("List is None")

    # p = self._head
    # # 只有一个元素的情况
    # if p.next is None:
    #     e = p.elem
    #     self._head = None
    #     print(e)
    #     return e

    # # 遍历计算链表长度
    # temp = 0
    # while p is not None:
    #     p = p.next
    #     temp += 1

    # # 删除并返回元素
    # p = self._head
    # num = 0
    # while p is not None:
    #     if num == (temp - n):

    #     p = p.next






    # 对链表的简单操作
mlist1 = LList()
for i in range(10):
    mlist1.prepend(i)
# for i in range(10):
#     mlist1.append(i)
mlist1.printAll()
# mlist1.pop_last()
mlist1.sort1()
mlist1.printAll()
# mlist1.for_each(print)




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