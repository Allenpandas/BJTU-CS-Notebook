Group = int(input())
for g_val in range(Group):
    n = int(input())
    squareDic = {}
    for n1 in range(n):
        temp = [int(item) for item in input().split()]
        for n2 in range(n):
            if temp[n2] in squareDic:
                if squareDic[temp[n2]][0] == n1:
                    squareDic[temp[n2]][1] = n2
            else:
                squareDic[temp[n2]] = [n1,n2]
    q = int(input())
    for i in range(q):
        x = int(input())
        if x in squareDic:
            print('%d %d'%(squareDic[x][0]+1,squareDic[x][1]+1))
        else:
            print(-1)
