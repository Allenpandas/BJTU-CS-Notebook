"""
XOR 异或操作 相同为0 相异为1
t 组数
1  第1组（共t组）的正整数1 找[0,1]
3  第1组（共t组）的正整数3 找[0,3]
4  第1组（共t组）的正整数4 找[0,4]

    0,1,2,4 都符合

输出：
Case #2: 2
Case #4: 3
Case #5: 4

"""

Group = int(input())
for g_val in range(Group):
    n = int(input())
    sum = 0
    for n1 in range(0, n+1):
        a = 2 * n1
        b = 3 * n1
        if a^b == n1:
            sum += 1
    print("Case #{}: {}".format(g_val+1, sum))
