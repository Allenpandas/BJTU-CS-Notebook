# 参考其他py代码
Group = int(input())
for g_val in range(Group):
    n, m = list(map(int, input().split()))
    s = [int(item) for item in input().split()]
    temp = [s[0]]
    for i in range(1, n):
        temp.append((2*temp[i-1]+s[i]) % m)
    sumN = [2*s[0]-1]
    for i in range(1, n):
        if s[i] == 1:
            sumN.append(2*temp[i-1] % m+1)
        else:
            sumN.append((2*temp[i-1]+2*s[i]) % m+sumN[i-1])
    print(sumN[n-1] % m)
