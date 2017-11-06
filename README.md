# python_learning
Data Structures and Algorithms in Python



### part2 抽象数据类型和Python类

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

