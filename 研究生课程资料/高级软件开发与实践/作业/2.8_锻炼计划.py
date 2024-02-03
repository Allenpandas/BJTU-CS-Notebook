#!/usr/bin/env python
# coding=utf-8
Group = int(input())
for g_val in range(Group):
    n = int(input())
    result = ''
    s = 9
    ans = 1

    # 判断第n个数有多少位
    while n > s * 2:
        n -= s * 2
        s *= 10
        ans *= 10
    ans += (s if n % s == 0 else n % s) - 1
    result = str(ans)  # 前半部分

    # n个位数为奇数，去掉最后一位
    if n - s <= 0:
        ans = int(ans / 10)
    while (ans):
        result += str(ans % 10)  # 后半部分
        ans = int(ans / 10)
    print(result)
