#!/usr/bin/env python
# coding=utf-8
import math
Group = int(input())  # 组数
for g_val in range(Group):
    input_str = input()
    if input_str != "":
        input_list = input_str.split()
        length = int(input_list[0])
        width = int(input_list[1])
        height = int(input_list[2])
        stick_len = float(input_list[3])  # 木条长度
        box_len = (math.sqrt(length * length + width * width + height * height))  # 盒子体对角线长度
        if box_len >= stick_len:
            print("Case #%d: YES" % (g_val + 1))
        else:
            print("Case #%d: NO" % (g_val + 1))
    else:
        break
