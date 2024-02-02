"""
1 组
2 2 10   N=2(件行李) M=2(家快递公司) D=10(自己最多可以拿D重量的行李)
5 6  N=2个整数,N=2件行李的重量
5 10 M=1行 第1家快递公司最多邮寄的重量a1=5 和费用c1=10
6 5  M=2行 第2家快递公司最多邮寄的重量a2=6 和费用c2=5
"""

Group = int(input())
for g_val in range(Group):
    N, M, D = map(int, input().split())
    ns = list(map(int, input().split()))
    ds = 0  # 行李总重量,默认0
    for i in ns:
        ds += i
    ms = []
    for i in range(M):
        ms.append(list(map(int, input().split())))
    if ds <= D:
        """无需快递公司"""
        print('Case #{}: {}'.format(g_val + 1, '0'))
    else:
        ds_last = ds - D  # 计算需要托运的重量
        sign = False
        temp = []
        for i in range(M):
            if ms[i][0] >= ds_last:
                sign = True
                temp.append(ms[i][1])
        if sign == False:
            print('Case #{}: {}'.format(g_val + 1, 'QAQ'))
        else:
            temp.sort()
            print('Case #{}: {}'.format(g_val + 1, temp[0]))
