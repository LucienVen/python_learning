#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# josephus问题和基于数组概念的解法

def josephus_A(n, k, m):
    people = list(range(1, n+1))

    i = k - 1

    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            
            if count == m:
                print(people[i], end="")
                people[i] = 0

            i = (i + 1) % n

        if num < n+1:
            print(", ", end="")
        else:
            print("")
    
    return
    

josephus_A(10, 2, 7)