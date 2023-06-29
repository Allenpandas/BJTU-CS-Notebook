# 定义一个整数变量age 编写代码判断年龄
age = 40

if 0 <= age <= 120:
    if age < 20:
        print("少年")
    elif 20 <= age < 40:
        print("青年")
    elif 40 <= age < 60:
        print("中年")
    else:
        print("老年")
else:
    print("年龄不正确")

