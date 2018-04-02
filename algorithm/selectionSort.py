#!/usr/bin/env python
# -*- coding:utf-8 -*-

def selection_sort(list):
    for fill_slot in range(len(list)-1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot+1):
            # print list[location]
            # print list[pos_of_max]
            if list[location] > list[pos_of_max]:
                pos_of_max = location

        list[fill_slot], list[pos_of_max] = list[pos_of_max], list[fill_slot]
        print "sorting list: {}".format(list)
    print '\n',"end list: {}".format(list)

if __name__ == '__main__':
    test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(test_list)
