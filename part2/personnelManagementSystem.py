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


# 学生类的实现
class Student(Person):
    _id_num = 0

    # 生成学号规则
    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year   # 获取入学年份
        return "1{:04}{:05}".format(year, cls._id_num) # 第二个参数为学生序号

    def __init__(self, name, sex, birthday, department):
        Person.__init__(self, name, sex, birthday, Student._id_gen())

        self._department = department   
        self._enroll_date = datetime.date.today()   # 入学年份
        self._courses = {} # 空字典，用以记录课程成绩

        # 选课方法
        def set_course(self, course_name):
            self._courses[course_name] = None   # 存入了上述字典，并把该课程对应的成绩value设为none

        # 设置成绩（前提必须选课）
        def set_score(self, course_name, score):
            # 判断是否已选择该课程
            if course_name not in self._courses:
                raise PersonValueError("No this course selected:", course_name)
            self._courses[course_name] = score

        # 列出所有成绩的列表
        def score(self):
            # ?????这语法.....骚啊
            return [(cname, self._courses[cname]) for cname in self._courses]

        # 获取学生细节（多态？）
        def details(self):
            return ", ".join((Person.details(self),
                                "入学日期：" + str(self._enroll_date),
                                "院系：", + str(self._department),
                                "课程记录：" + str(self.score())
                                ))



