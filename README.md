# python_learning
Data Structures and Algorithms in Python



## part2 抽象数据类型和Python类

#### 构造有理数类ADT

```python
ADT Rational:							#定义有理数的抽象类型
	Rational(self, int num, int den)	#构造有理数num/den
    +(self, Rational r2)				#求出本对象加r2的结果(有理数)
    -(self, Rational r2)				#求出本对象减r2的结果
    *(self, Rational r2)				#求出本对象乘r2的结果
    /(self, Rational r2)				#求出本对象除r2的结果
    num(self)
    den(self)
```





#### 学校人事管理系统中的类设计

##### 基础人员ADT设计

```python
ADT Person:														# 定义人员抽象数据类型
    Person(self, str name, str sex, tuple birthday, str ident)	# 构造人员对象
    id(self)	# 取得该人员记录中的人员编号
    name(self)	# 取得名称
    sex(self)	# 取得性别
    birthday(self)	# 取得出生年月
    age(self)	# 取得年龄
    set_name(self, str name) # 修改人员姓名
    <(self, Person another)	# 基于人员编号比较两个记录
    details(self)	# 给出人员记录里保存的数据详情
```







## part3 线性表

#### 单链表类的实现

```python
ADT List:				# 一个表抽象数据类型
    List(self)			# 表构造操作，创建一个新表
    is_empty(self)		# 判断self是否为一个空表
    len(self)			# 获取self的长度
    prepend(self, elem)		# 将元素elem加入表中作为第一个元素
    append(self, elem)		# 将元素elem加入表中作为最后一个元素
    insert(self, elem, i)		# 将元素elem加入表中最为第i个元素，其他元素的顺序不变
    del_first(self)			# 删除表中的首元素
    del_last(self)			# 删除表中的尾元素
    del(self, i)			# 删除表中第i个元素
    search(self, elem)		# 查找元素elem在表中出现的位置，不存在时返回-1
    forall(self, op)		# 对表中的每个元素执行操作op
```

