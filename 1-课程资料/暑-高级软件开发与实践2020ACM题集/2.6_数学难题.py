#!/usr/bin/env python
# coding=utf-8
Group = int(input())
for g_val in range(Group):
    num = int(input())
    result = 0
    for i in range(1, num + 1):
        temp = 1
        for n2 in range(2, i + 1):
            temp *= n2
        result += temp
    print(result)
