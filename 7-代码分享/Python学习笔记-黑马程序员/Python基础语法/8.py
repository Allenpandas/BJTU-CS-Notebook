# class PrintMessage:
#     """一个打印信息的类"""
#     date = '2022-05-15'
#
#     def __init__(self, i):
#         self.month = i
#         print("这是构造方法")
#
#     def f1(self):
#         return 'hello world'
#
#     def f2(self):
#         return 'welcome to China'
#
#
# x = PrintMessage()
#
# # print("PrintMessage类的属性date为：", x.date)
# # print("PrintMessage类的方法f1为：", x.f1())
# # print("PrintMessage类的方法f2为：", x.f2())

#
# class PrintMessage:
#     """一个打印信息的类"""
#
#     def __init__(self, month):
#         self.month = month
#         print("这是构造方法")
#
#
# x = PrintMessage('5月')
# print("当前月份为：", x.month)


# class Person:
#     """定义类的基本属性"""
#     name = ''
#     age = 0
#     """私有属性用__开头"""
#     __weight = 0
#
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.__weight = weight
#
#     def speak(self):
#         print("姓名:", self.name, ',年龄:', self.age, "体重:", self.__weight)
#
#
# class Student(Person):
#     """定义类的基本属性"""
#     grade = ''
#     def __init__(self, name, age, weight, grade):
#
#         # 继承父类的构造函数
#         Person.__init__(self, name, age, weight)
#         # 自己的构造函数，给成员属性赋值
#         self.grade = grade
#
#     def speak(self):
#         print("我是:", self.name, ', 年龄:', self.age, ", 年级为:", self.grade)
#
#
# student1 = Student('allenpandas', '25', '75kg', '研究生一年级')
# student1.speak()


# class Parent:
#     def speak(self):
#         print('这是父类的方法')
#
#     def eat(self):
#         print('这是父类的方法')
#
#
# class Student(Parent):
#     def speak(self):
#         print('这是子类的方法')
#
#
# student1 = Student()
# student1.speak()
# student1.eat()


# class Student:
#     age = 18
#     __weight = '60kg'
#
#     def speak(self):
#         print('这是共有方法')
#
#     def __speak(self):
#         print('这是私有方法')
#
#
# # 实例化
# student1 = Student()
# print("student1的公有属性age为:", student1.age)
# print("student1的私有属性__weight为:", student1.__weight)


class Student:

    def speak(self):
        print('这是共有方法')

    def __speak(self):
        print('这是私有方法')


# 实例化
student1 = Student()

student1.speak()
student1.__speak()