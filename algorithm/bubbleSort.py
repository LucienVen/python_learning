#!/usr/bin/env python
# -*- coding:utf-8 -*-

def bubble_sort(list):
    exc = True
    pass_num = len(list) - 1
    temp = 0

    while pass_num > 0 and exc:
        exc = False
        sort = 0

        for i in range(pass_num):
            if list[i] > list[i+1]:
                exc = True
                list[i], list[i+1] = list[i+1], list[i]
                sort += 1

        temp += 1
        print "第{0}次排序,交换{1}次: {2}".format(temp, sort, test_list)
        pass_num = pass_num - 1

if __name__ == '__main__':
    test_list=[2, 46, 70, 99, 6, 18, 100, 76, 100, 10]
    bubble_sort(test_list)
    print '\n',"end list: {}".format(test_list)
