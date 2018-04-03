#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 排序算法


def BulleSort(sort_list):
    ''' 冒泡排序 '''
    print('原数组：', sort_list)
    n = len(sort_list)
    for i in range(n):
        # 优化，标记完成点
        flag = 1
        for j in range(1, n):
            if sort_list[j-1] > sort_list[j]:
                sort_list[j-1], sort_list[j] = sort_list[j], sort_list[j-1]
                # else:
                flag = 0

            print('sorting:', sort_list)

        if flag:
            break


    print('冒泡排序: ', sort_list)
    print('-'*30)


def InsertSort(sort_list):
    ''' 插入排序 '''
    ary = sort_list
    print("原数组：", ary)
    n = len(ary)
    for i in range(1,n):
        if ary[i] < ary[i-1]:
            temp = ary[i]
            index = i           #待插入的下标
            for j in range(i-1,-1,-1):  #从i-1 循环到 0 (包括0)
                # i=1,j=0; i=2,j=1,0; i=3,j=2,1,0 ...
                if ary[j] > temp :
                    ary[j+1] = ary[j]
                    index = j   #记录待插入下标
                else :
                    break
                # print("sorting:", ary)


            ary[index] = temp
        print("one sorting:", ary)

    print('插入排序：', ary)



def main():
    sort_list = [5,7,2,9,3,6]
    print('-'*30)
    BulleSort(sort_list)

    sort_list = [5,7,2,9,3,6]
    InsertSort(sort_list)

if __name__ == '__main__':
    main()
