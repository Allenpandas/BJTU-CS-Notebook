#!/usr/bin/env
# python
# coding=utf-8
"""
输入：
1    1组数据
3 3  花坛长度为n=3(接下来有3行) 花坛宽度为m=3（3个元素，即3颗花）
ABC  第1行 m=3个元素
BBC  第2行 m=3个元素  BB 表示相同花
CCC  第3行 m=3个元素

输出：
3    :k=3,标识有3种花（不同的字母）
5 C  :C花个数为5
3 B  :B花个数为3
1 A  :A花个数为1
"""

Group = int(input())
for g_val in range(Group):
    n, m = list(map(int, input().split()))  # n行 m个元素
    types = {}  # 定义type，key为种类 value为数量
    for n_val in range(n):
        rowStr = input()  # 每排花的内容，如：ABC
        row = list(rowStr)  # ['A', 'B', 'C']
        for row_val in row:
            if types.__contains__(row_val):
                types[row_val] += 1
            else:
                types[row_val] = 1
    result = sorted(types.items(), key=lambda x: (-x[1], x[0]))
    # print(result);exit()
    print(len(result))
    for item in result:
        print('%d %s' % (item[1], item[0]))
