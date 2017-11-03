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
