#!/usr/bin/env python
# coding=utf-8
Group = int(input())
for g_val in range(Group):
    today = int(input())  # 今天菜品编号
    n = int(input())  # N顿饭
    input_str = input()
    input_list = input_str.split()
    flag = "happy"  # 默认女朋友是高兴的
    for list_val in input_list:
        if int(list_val) == today:
            flag = "unhappy"
            break
    print("%s" % flag)
