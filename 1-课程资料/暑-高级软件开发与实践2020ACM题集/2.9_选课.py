#!/usr/bin/env python
# coding=utf-8
Group = int(input())
for g_val in range(Group):
    classN = {}
    input_str = input().split()
    n = int(input_str[0])  # 班级人数
    p = int(input_str[1])  # p%选课比例
    # n, p = list(map(int,input().split()))
    limit = int(n * p / 100)  # 计算p%得有多少人选课
    for i in range(n):
        temp = [int(item) for item in input().split()]
        for temp1 in temp:
            if temp1 in classN:
                classN[temp1] += 1
            else:
                classN[temp1] = 1
    result = sorted(classN.items(), key=lambda x: -x[1])  # 升序
    # print(result)
    if limit >= int(result[2][1]):
        print('no')
    else:
        print('yes')
