#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 有理数类的定义
class Rational:
    @staticmethod  # 静态方法：辗转相除法求最大公约数
    def _gcd(m, n):
        if n == 0:
            m, n = n, m
        while m != 0:
            m, n = m % n, m
        return n

    # 初始化
    def __init__(self, num, den):
        # 检查
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError

        sign = 1
        if num < 0:
            num, sign = -num, -sign
        if den < 0:
            den, sign = -den, -sign

        # 求最大公约数
        g = Rational._gcd(num, den)

        self._num = sign * (num // g)
        self._den = den // g

    # 解析操作(提供方法返回内部属性)
    def num(self):
        return self._num
    def den(self):
        return self._den

    # 实例方法
    def __add__(self, another):
        den = self._den * another.den()
        num = (self._num * another.den() + self._den * another.num())
        return Rational(num, den)

    # 特殊方法名：+ __add__; - __sub__; * __mul__; // __floordiv__ ;  .........

    # 有理数相等
    def __eq__(self, another):
        return self._num * another.den() == self._den * another.num()

    # 有理数小于 __lt__

    # 对象转换到字符串
    # 有理数的字符串转换方法
    def __str__(self):
        return str(self._num) + "/" + str(self._den)

    def print(self):
        print(self._num, "/", self._den)




def main():
    p = Rational(12, 60)
    print(p.num())
    print(p.den())
    p.print()


if __name__ == '__main__':
    main()
