# 2.3循环遍历
# 实际开发中，对元组的循环遍历需求并不多,除非确认元组中的数据类型
#
# info_tuple = ("zhangsan", 18, "178cm")
# # # 迭代遍历
# # for my_info in info_tuple:
# #     print(my_info)
# #
# #
# # info_tuple = ("alen", 25, "178cm", "男")
# # for my_data in info_tuple:
# #     print(my_data)


# 2.4实际应用场景
# 1.作为函数的参数和返回值
# 2.格式化字符串
# 3.保护数据安全


# %s() 后面本质是一个元组
#
# print("姓名:%s, 年龄:%d, 身高:%.2fm" % ("小明", 18, 1.75))
#
# # 等价写法1:
# user_tuple = ("小明", 18, 1.75)
# print("姓名:%s, 年龄:%d, 身高:%.2fm" % user_tuple)
#
# # 等价写法2:
# info_str = "姓名:%s, 年龄:%d, 身高:%.2fm" % user_tuple
# print(info_str)



# # list元组转成列表
#
# num_list= [1,2,3,4]
# print(type(num_list))
# num_tuple = tuple(num_list)
# print(type(num_tuple))

# # tuple列表转成元组
str_tuple = ("zhangsan", 1, 2)
print(type(str_tuple))
str_list = list(str_tuple)
print(type(str_list))


