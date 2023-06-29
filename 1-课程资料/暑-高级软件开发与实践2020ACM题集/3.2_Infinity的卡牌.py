# !/usr/bin/env python
# coding=utf-8
Group = int(input())
for g_val in range(Group):
    n = int(input())  # 牌总数
    input_list = input().split()  # 剩余牌的牌号,如: 1 1 2 3 3
    temp = {}
    for item in input_list:
        if item in temp:
            temp[item] = 0
        else:
            temp[item] = 1
    result = sorted(temp.items(), key=lambda x: (-x[1]))
    print('Case #%d: %d' % (g_val + 1, int(result[0][0])))
