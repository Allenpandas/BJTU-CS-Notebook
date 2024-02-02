#!/usr/bin/env python
# coding=utf-8
# 找到最大值跟[0]交换位置 找到最小值跟[n]交换位置
Group = int(input())  # 组数
for g_val in range(Group):
    input_str = input()
    if input_str != "":
        length = int(input_str[0])  # 每组数的个数
        input_list = input_str.split()
        max_location = 1  # 默认第1个数所在位置是最大值,从第2个开始遍历比大小
        for i in range(2, length + 1):
            if int(input_list[i]) > int(input_list[max_location]):
                max_location = i
        temp = input_list[max_location]
        input_list[max_location] = input_list[1]
        input_list[1] = temp

        min_location = int(length)  # 默认第n个数所在位置是最小值
        for i in range(2, length):
            if int(input_list[i]) < int(input_list[min_location]):
                min_location = i
        temp = input_list[min_location]
        input_list[min_location] = input_list[length]
        input_list[length] = temp
        print("Case #%d: %s" % (g_val + 1, " ".join(str(i) for i in input_list[1:])))
    else:
        break