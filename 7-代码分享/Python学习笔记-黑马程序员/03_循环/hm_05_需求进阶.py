result = 0

# 循环时的计数器变量
i = 0

while i <= 100:
    if i % 2 == 0:

        # 当>2时才累加
        result += i
        # print(i)

    i += 1

print("0~100之间的偶数累加结果 = %d" % result)