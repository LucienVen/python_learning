#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 哈希查找
# 散列表 -> 散列函数 -> 值/数据
import time

class HashTable:
    # 构造函数
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    # put data in slot   把数据放入插槽
    def put_data_in_slot(self, key, data, slot):
        # 检查该位置是否为空，若空，则插入数据
        if self.slots[slot] == None:
            # 这样，算是定义了一个字典麽？？？
            # 定义了两个list
            self.slots[slot] = key
            self.data[slot] = data
            return True
        # 如果不为空，检查该位置是否已存有数据，所data_now == data_late， 复写一次
        else:
            if self.slots[slot] == key:
                self.data[slot] = date
                return True
            else:
                return False

    #  取模，插入
    def hash_funciton(self, key, size):
        return key % size

    # 处理聚集   开放寻址（线性寻找， +1）
    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    # 数据插入hash表
    def put(self, key, data):
        slot = self.hash_funciton(key, self.size)
        result = self.put_data_in_slot(key, data, slot)
        while not result:
            slot = self.rehash(slot, self.size)
            result = self.put_data_in_slot(key, data, slot)


    # hash查找
    def get(self, key):
        start_slot = self.hash_funciton(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position == self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data


    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)





if __name__ == '__main__':
    table=HashTable();
    table[54]='cat';
    table[26]='dog';
    table[93]='lion';
    table[17]="tiger";
    table[77]="bird";
    table[44]="goat";
    table[55]="pig";
    table[20]="chicken";
    # print table.slots;
    # print table.data;
