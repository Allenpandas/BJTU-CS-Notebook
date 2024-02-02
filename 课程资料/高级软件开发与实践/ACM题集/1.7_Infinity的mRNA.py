#!/usr/bin/env python
# coding=utf-8


def trans(str):
    """定义函数:A变成U, U变成A, C变成G, G变成C"""
    if str == 'A':
        return 'U'
    elif str == 'U':
        return 'A'
    elif str == 'C':
        return 'G'
    elif str == 'G':
        return 'C'
    else:
        return False


Group = int(input())  # 组数
for g_val in range(Group):
    input_str = input()
    if input_str != "":
        str = ""
        for chars in range(len(input_str)):
            str += trans(input_str[chars])
        print("Case #%d: %s" % (g_val + 1, str))
    else:
        break
