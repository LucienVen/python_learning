#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 批量修改/替换doc内容

# import sys
from docx import Document

path = r"/Users/taozz/Dropbox/projectCode/python/python_learning/other/logfile/网易商城_陈晓彬_第二周.docx"


def main():
    document = Document(path)
    # 读取文档中所有的段落列表
    tables = document.tables
    tables[0].cell(0, 1).text = "201441410237"
    tables[0].cell(0, 3).text = "14软件工程1班"
    tables[0].cell(1, 1).text = "梁祥桃"

    tables[1].cell(1, 1).text = "项目经理：梁祥桃"
    document.save("demo.docx")


if __name__ == '__main__':
    main()
