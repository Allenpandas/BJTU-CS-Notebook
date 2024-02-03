#!/usr/bin/env python
# coding=utf-8
"""
1   1组数据
2 5 2   n,m,k  n行 m列 k对好朋友
aBA..    第1行（共n=2行） m=5个字符串  B和b是好朋友
...b.   第2行（共n=2行） m=5个字符串

"""

T = int(input())
for t1 in range(T):
    ns = [int(item) for item in input().split()]
    nm = []
    for i in range(ns[0]):
        temp = input()
        nm.append(temp)
    step1 = []
    step2 = []
    for i in range(ns[2]):
        check = 0
        for r in range(ns[0]):
            for c in range(ns[1]):
                if nm[r][c] == chr(97+i):
                    step1.append([r, c])
                    check += 1
                if nm[r][c] == chr(65+i):
                    step2.append([r, c])
                    check += 1
                if check == 2:
                    break
            if check == 2:
                break
    results = []
    for i in range(len(step1)):
        results.append(abs(step2[i][0]-step1[i][0])+abs(step2[i][1]-step1[i][1]))
    minIndex = 0
    for i in range(1, len(results)):
        if results[i] < results[minIndex]:
            minIndex = i
    print(chr(97+minIndex))
