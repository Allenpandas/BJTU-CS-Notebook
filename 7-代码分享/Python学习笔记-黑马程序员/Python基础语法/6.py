# list = [1,2,3,4]
# it = iter(list)
# for x in it:
#     print(x)


# list = [1,2,3,4]
# it = iter(list)
# while(True):
#     print(next(it))

#
# def max(a, b):
#     if a < b:
#         return b
#     else:
#         return a
#
#
# value = max(3, 5)
# print(value)


# def print_info(name, age=20):
#     """打印年龄和姓名"""
#     print("姓名：", name, "，年龄：", age)
#     return
#
#
# print_info(name='allenpandas')



# def print_info(*var_tuple):
#     print(var_tuple)
#
#
# print_info(10, 'allenpandas', '女')


x = lambda a: a * 10
print(x(5))
