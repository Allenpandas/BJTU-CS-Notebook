import math

Group = int(input())
for g_val in range(Group):
    inputStr = input()
    if inputStr != "":
        M = 0
        N = int(inputStr)
        # 利用等差数列前N项和公式,求出前N项和Sn和n的关系
        # Sn = na1 + n(n-1)d/2  a1=1, d=1  =>  Sn = n * n + n
        # 利用求根公式得到 n = math.sqrt(N+1/4)-1/2
        maxN = int(math.sqrt(2*N+1/4)-1/2)

        for n1 in range(2, maxN+1):
            a1 = int((2*N-n1*(n1-1))/(2*n1))
            if a1 == 0:
                continue
            elif n1*(2*a1+n1-1)/2 == N:
                M += 1
        print("Case #%d: %d" % (g_val + 1, M))
    else:
        break
