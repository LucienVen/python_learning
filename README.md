# python_learning
Data Structures and Algorithms in Python



### part2 抽象数据类型和Python类

##### 构造有理数类ADT

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

