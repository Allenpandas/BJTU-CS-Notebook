# def sum_2_number(num1, num2):
#     result = num1 + num2
#     print("%d + %d = %d" %(num1, num2, result))
#     return result
#
#
# result = sum_2_number(10, 22)
# print("计算的结果为%d" % result)


# 函数嵌套练习
# 需求1：使用*打印分割线
# def print_line():
#     print("*" * 50)
#     return
#
#
# print_line()

# 需求2：打印一个由任意字符组成的分割线
# def print_line2():
#     print("-" * 50)
#     return
#
#
# print_line2()

# 需求3：打印任意字符，打印任意重复次数
# def print_line3(char, times):
#     print(char * times)
#     return
#
#
# print_line3("*", 80)


# 需求4 连续打印5行
# def print_line4(char, times):
#     """定义函数,自定义打印内容"""
#     print(char * times)
#     return
#
#
# def print_line41():
#     """定义函数,使用while循环执行"""
#     row = 0
#     while row < 5:
#         print_line4("*", 50)
#         row += 1
#     return
#
#
# print_line41()


def print_line5(char, times):
    """打印多行分割线

    :param char: 分割线使用的分割字符
    :param times: 分割线重复的次数
    :return:
    """
    print(char * times)
    return


print_line5("+", 50)









