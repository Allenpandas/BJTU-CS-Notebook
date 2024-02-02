#!/usr/bin/env python
# coding=utf-8
Group = int(input())  # 测试数据组数
for g_val in range(Group):
    primary = 0  # 低级
    middle = 0  # 中级
    high = 0  # 高级
    number = int(input())  # 简历份数
    for num_v in range(number):
        input_str = input()
        if input_str != "":
            score = input_str.split()
            """指定下标获取初、中、高级分数,先判断高级,最后判断初级成绩"""
            if int(score[2]) >= 60:  # 高级
                primary += 1
                middle += 1
                high += 1
            elif int(score[1]) >= 60:  # 中级
                primary += 1
                middle += 1
            elif int(score[0]) >= 60:  # 初级魔法课成绩
                primary += 1
        else:
            break
    print("Case #%d: %d %d %d" % (g_val + 1, primary, middle, high))
