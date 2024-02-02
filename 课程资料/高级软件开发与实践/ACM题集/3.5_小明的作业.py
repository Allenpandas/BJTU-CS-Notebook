"""
1/3 = 0.3333333333333333 目前支持16位 > 9位
0.1234 1234 1234 1234 循环节1234
"""
Group = int(input())
for g_val in range(Group):
    input_str = input().split()
    a = int(input_str[0])
    b = int(input_str[1])
    container = []
    result = str(int(a / b)) + '.'  # 获取整数部分和小数点
    status = False  # 状态位
    for i in range(9):
        temp = a * 10 % b
        if temp == 0:
            break
        else:
            if temp in container:
                status = True
                break
            else:
                result += str(int(a * 10 / b))
                a = temp
                container.append(temp)
    if status:
        print('Case #%d: %s' % (g_val + 1, result))
    else:
        print('Case #%d: heiheihei' % (g_val + 1))

