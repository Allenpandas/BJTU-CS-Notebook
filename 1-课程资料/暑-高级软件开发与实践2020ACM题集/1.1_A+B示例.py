#!/usr/bin/env python
# coding=utf-8

while 1:
    a = []
    str = input()
    if str != '':
        for x in str.split():
            a.append(int(x))
        print(sum(a))
    else:
        break
