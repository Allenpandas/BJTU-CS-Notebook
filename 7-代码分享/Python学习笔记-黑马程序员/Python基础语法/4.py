# print(4 + 5)
# print(4 - 5)
# print(4 * 5)
# print(102 / 5)
# print(102 % 5)
# print(2**3)
# print(102 // 5)


# list = [1,2,3,4,5]
# if 2 in list:
#     print("2 在序列中")
#
# if 10 not in list:
#     print("10 不在序列中")


# a = 10
# b = 10
# if a is b:
#     print(1111)


age = int(input("请输入你们家狗狗的年龄："))
print("")
if age <= 0:
    print("年龄非法！")
elif age == 1:
    print("相当于14岁人的年龄~")
elif age == 2:
    print("相当于22岁人的年龄~")
elif age > 2:
    human_age = 22 + (age - 2) * 5
    print("对应人的年龄为:", human_age)

# input("输入enter键（回车键）退出")
