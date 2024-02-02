#!/usr/bin/env python
# coding=utf-8

# 遇到24一律按I处理
Group = int(input())  # 组数
for g_val in range(Group):
    input_list = input().split()
    length = int(input_list[0])  # 密码长度Mi

    code = ""  # 默认密码给初始值""
    for i in range(1, length + 1):
        """遍历元素[1,length+1]"""
        s = int(int(input_list[i]) / 10)  # 十位数
        g = int(input_list[i]) % 10  # 个位数
        if s == 1 and g == 1:
            code += 'A'
        elif s == 1 and g == 2:
            code += 'B'
        elif s == 1 and g == 3:
            code += 'C'
        elif s == 1 and g == 4:
            code += 'D'
        elif s == 1 and g == 5:
            code += 'E'

        elif s == 2 and g == 1:
            code += 'F'
        elif s == 2 and g == 2:
            code += 'G'
        elif s == 2 and g == 3:
            code += 'H'
        elif s == 2 and g == 4:
            code += 'I'  # 遇到24按I处理
        elif s == 2 and g == 5:
            code += 'K'

        elif s == 3 and g == 1:
            code += 'L'
        elif s == 3 and g == 2:
            code += 'M'
        elif s == 3 and g == 3:
            code += 'N'
        elif s == 3 and g == 4:
            code += 'O'
        elif s == 3 and g == 5:
            code += 'P'

        elif s == 4 and g == 1:
            code += 'Q'
        elif s == 4 and g == 2:
            code += 'R'
        elif s == 4 and g == 3:
            code += 'S'
        elif s == 4 and g == 4:
            code += 'T'
        elif s == 4 and g == 5:
            code += 'U'

        elif s == 5 and g == 1:
            code += 'V'
        elif s == 5 and g == 2:
            code += 'W'
        elif s == 5 and g == 3:
            code += 'X'
        elif s == 5 and g == 4:
            code += 'Y'
        elif s == 5 and g == 5:
            code += 'Z'
    print("Case #%d: %s" % (g_val + 1, code))
