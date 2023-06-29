def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


Group = int(input())
for g_val in range(Group):
    n = int(input())
    count = 0  # 陷阱个数
    for x in range(1, n + 1):

        # 第x行的陷阱个数为：n - gcd(x, n)
        count += n - gcd(x, n)
    print('Case #%d: %d' % (g_val + 1, count))


# 第i行陷阱个数(不能被n整除的数) + 能被n整除的数 = 总数n
# 能被n整除的数的个数 =  gcd(n, x)
