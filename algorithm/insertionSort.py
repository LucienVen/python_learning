#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 插入排序
def insertion_sort(list):
    for index in range(1, len(list)):
        current_value = list[index]
        position = index
        while position > 0 and list[position - 1] > current_value:
            print '比较项>>> list[position]: {} -- current_value: {}'.format(list[position - 1], current_value)
            list[position] = list[position - 1]
            position = position - 1
        list[position] = current_value
        print "sorting list: {}".format(list)


# def insertion_sort_binarysearch(list):
#     for index in range(1, len(list))



if __name__ == '__main__':
    test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(test_list)
    print test_list
