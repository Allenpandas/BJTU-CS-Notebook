#!/usr/bin/env python
# coding=utf-8


def gcd(a, b):
    """辗转相除求最大公约数"""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


Group = int(input())
for g_val in range(Group):
    input_str = input()
    if input_str != "":
        input_list = input_str.split()
        n = int(input_list[0])
        m = int(input_list[1])
        result = gcd(n, m)
        print("Case #%d: %d" % (g_val + 1, n / result))
    else:
        break
