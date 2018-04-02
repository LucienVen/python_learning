# -*- coding:utf-8 -*-
import time
def quicksort(a):
     if len(a) <= 1:
         return a
    #  '''如果a為一位數則直接傳回a'''

     return quicksort([x for x in a[1:] if x < a[0]]) + \
            [a[0]] + quicksort([x for x in a[1:] if x > a[0]])
        #    '''輸出排序後的比a[0]小的數列'''   #  '''+\為空格'''


        #   '''輸出a[0]'''

    #  '''輸出排序後的比a[0]大的數列'''

list = [1,2,4,897,5,232,78,1,0,77,65,22,589,5,15]
start = time.time()
print quicksort(list)
end = time.time()
runingtime = end - start

print runingtime
