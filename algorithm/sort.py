#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 排序算法


def BulleSort(sort_list):
    ''' 冒泡排序 '''    
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
    
        


def main():
    sort_list = [5,7,2,9,3,6]
    print(sort_list)
    print('-'*30)
    BulleSort(sort_list)

if __name__ == '__main__':
    main()
