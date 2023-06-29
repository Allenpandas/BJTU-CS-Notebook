# !/usr/bin/env python
# coding=utf-8
"""

"""
Group = int(input())
for g_val in range(Group):
    n = int(input())
    a = [int(item) for item in input().split()]
    sigma1 = [0]
    sigma2 = [0]
    for i in range(1,n+1):
        sigma1.append(sigma1[i-1] + a[i-1])
        sigma2.append(sigma2[i-1] + a[i-1] * i)
    q = int(input())
    print("Case #%d: " % (g_val + 1))
    for q1 in range(q):
        rangeL, rangeR = list(map(int, input().split()))
        result = sigma2[rangeR] - sigma2[rangeL-1] - ((sigma1[rangeR] - sigma1[rangeL-1])*(rangeL-1))
        print("%d" % (result))
