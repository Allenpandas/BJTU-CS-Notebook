#!/usr/bin/env python
# coding=utf-8
Group = int(input())
for g_val in range(Group):
    input_str = input()
    input_list = input_str.split()
    a = int(input_list[0])  # 底数
    k = int(input_list[1])  # 指数
    value = len(str(a ** k))
    print("%d" % value)
