#!/usr/bin/env python
# coding=utf-8
Group = int(input())  # 组数
for g_val in range(Group):

    input_str = str(input())
    if input_str != "":
        num = int(input_str)  # 获取输入的整数num

        if '2333' in input_str:
            result = num  # 如果包含2333,所求即所输
        while 1:
            """若不包含2333,从num开始逐个+1,再判断是否包含2333"""
            num += 1
            if "2333" in str(num):
                result = num
                break
            else:
                continue

        print("Case #%d: %d" % (g_val + 1, result))
    else:
        break
