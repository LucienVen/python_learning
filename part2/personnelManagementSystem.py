#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 类定义实例：人事管理系统的类实现

import datetime


# 定义异常类
class PersonTypeError(TypeError):
    pass

class PersonValueError(ValueError):
    pass

# 公共人员类的实现
class Person:
    _num = 0

    @classmethod    # 定义类方法，取得人员计数
    def num(cls):
        return Person._num


    def __init__(self, name, sex, birthday, ident):
        if not (isinstance(name, str)) and sex in ("女", "男"):
            raise PersonValueError(name, sex)

        try:
            birthday = datetime.date(*birthday) # 生成一个日期对象
        except:
            raise PersonValueError("Wrong date:", birthday)

        self._name = name
        self._sex = sex
        self._birthday = birthday
        self._id = ident
        
        # 实例计数
        Person._num += 1

    def id(self):
        return self._id

    def name(self):
        return self._name

    def sex(self):
        return self._sex
    
    def birthday(self):
        return self._birthday

    def age(self):
        return (datetime.date.today().year - self._birthday.year)

    # 修改名字
    def set_name(self, name):
        if not isinstance(name, str):
            raise PersonValueError("set_name", name)
        self._name = name

    def __lt__(self, another):
        if not isinstance(another, Person):
            raise PersonTypeError(another)
        raise self._id < another._id

    # 输出有关的类
    def __str__(self):
        return " ".join((self._id, self._name, self._sex, str(self._birthday)))

    def details(self):
        return " ".join(("编号：" + self._id,
                        "姓名：" + self._name,
                        "性别：" + self._sex,
                        "出生日期：" + str(self._birthday)))