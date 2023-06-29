#!/usr/bin/env python
# coding=utf-8
Group = int(input())
for g_val in range(Group):
    input_str = input()
    if input_str != "":
        input_list = input_str.split()
        a = int(input_list[0]) * int(input_list[1])
        b = int(input_list[0]) * int(input_list[2])
        c = int(input_list[1]) * int(input_list[2])
        print("Case #%d: %d" % (g_val+1, max(a, b, c)))
    else:
        break
