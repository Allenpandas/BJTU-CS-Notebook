"""
n=1 组成一个9*9的十字架
n=2 外面再套一层,组成一个13*13的十字架
n=3 外面再套一层,组成17*17的十字架
每加一层,边长+4
边长 = 5 + n * 4

"""

Group = int(input())
for g_val in range(Group):
    n = int(input())
    rc = 5 + 4 * n  # 矩阵阶数
    square = [['.']*rc for i in range(rc)]  # 矩阵初始化
    for j in range(rc // 2 - 2,rc // 2 + 3):    # 画中心十字
        square[rc // 2][j] = square[j][rc // 2 ] = '$'
    for j in range(1, n+1):  # x,y为矩阵点坐标
        x = j * 2
        y = 2 * j - 1
        square[x][y] = square[x][y + 1] = square[x - 1][y + 1] = '$'    # 左上角
        y = rc - j * 2 - 1
        square[x][y] = square[x][y + 1] = square[x - 1][y] = '$'    # 右上角
        x = rc - j * 2 - 1
        square[x][y] = square[x][y + 1] = square[x + 1][y] = '$'    # 右下角
        y = 2 * j - 1
        square[x][y] = square[x][y + 1] = square[x + 1][y + 1] = '$'    # 左下角
        for jj in range(j * 2,rc - j * 2):  # 旋转赋值，能节省一层循环
            square[jj][(j - 1) * 2 ] = square[(j - 1) * 2 ][jj] = square[rc - (j - 1) * 2 - 1][jj] = square[jj][rc - (j - 1) * 2 - 1] = '$'
    print("Case #%s:" % (g_val + 1))
    for i in range(rc):
        print("".join(square[i]))   # 将数组转为字符串输出
