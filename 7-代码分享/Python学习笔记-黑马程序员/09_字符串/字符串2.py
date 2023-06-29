# 判断空白字符
# space_str = " "
# print(space_str.isspace())


# \n \t \r 都代表空白字符
# space_str2 = " \n\t\r"
# print(space_str2.isspace())


# 1>都不能判断小数
num_str = "1.1"
# 2> unicode 字符串
num_str = "(1)"

print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())
