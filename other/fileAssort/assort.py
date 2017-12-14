#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 文件分类

import os
import shutil

path = '/Users/taozz/Downloads'

photo_path = '/Users/taozz/Downloads/photo'

suffix = []

files = os.listdir(path)


for item in files:
    if (not os.path.isdir(item)):
        # print(os.path.splitext(item)[1])
        file_suffix = os.path.splitext(item)[1]
        if file_suffix in suffix:
            pass
        else:
            suffix.append(file_suffix)

        if file_suffix in ['.jpg', '.JPG', '.PNG', '.png', '.jpg-large', '.psd']:
            old_path = os.path.join(path, item)
            if(shutil.move(old_path, photo_path)):
                print("Remove photo: {}".format(item))
            else:
                print("Remove failed: {}".format(item))



for i in suffix:
    print(i)
