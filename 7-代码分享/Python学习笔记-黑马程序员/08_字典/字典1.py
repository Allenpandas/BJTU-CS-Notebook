# 1定义
"""
字典是除了列表之外最灵活的数据类型

字典和列表的区别:
列表存储有序的对象集合
字典存储无序的对象集合,字典使用键值对来存储数据 键和值之间使用:分割

字典使用{}来定义
字典使用键值对存储数据，键值对之间用逗号","隔开。

键只能是字符串、数字、元组，且唯一
值可以取任何的数据类型
"""

# 2定义
# user_info = {"name": "小明",
#              "age": 18,
#              "sex": "男",
#              "height": 1.75}
# print(user_info)


# 3基本使用
# xiaoming_dict1 = {"name": "小明"}
# # 取值
# print(xiaoming_dict1["name"])
# # 取值时，key不存在会报错
# print(xiaoming_dict1["sex"])



# 增加
# xiaoming_dict2 = {"name": "小明"}
# xiaoming_dict2["age"] = 18
# xiaoming_dict2["name"] = "alen"
# print(xiaoming_dict2)


# 删除
# xiaoming_dict = {"name": "小明", "age":18}
# xiaoming_dict.pop("name")
# print(xiaoming_dict)


# 统计键值对的数量
# xiaoming_dict = {"name": "wuyalun",
#                  "age": 25}
# print(len(xiaoming_dict))


# a_dict = {"name": "alen",
#           "age": 25,
#           "school": "bjtx-cit"}
# print(len(a_dict))



# 合并字典
# temp_dict = {"height": 1.75}
# xiaoming_dict = {"name": "wuyalun",
#                  "age": 25}
# # 若key存在,则更新value值,若不存在key 新增key-value
# xiaoming_dict.update(temp_dict)
# print(xiaoming_dict)



# 清空字典(清空所有元素)
# xiaoming_dict = {"name": "wuyalun",
#                  "age": 25}
# xiaoming_dict.clear()
# print(xiaoming_dict)

# xiaoming_dict = {"name": "xiaoming",
#                  "age": 25}
# xiaoming_dict.clear()
# print(xiaoming_dict)



# xiaoming_dict = {"name": "xiaoming",
#                  "age": 25,
#                  "height": 1.75}
# # 循环遍历需求不多
# for k in xiaoming_dict:
#     print("键为:%s, 值为:%s" %(k, xiaoming_dict[k]))

# 列表和字典结合应用
card_list = [
    {"name": "张三", "age": 18},
    {"name": "李四", "age": 20},
    {"name": "王五", "age": 25}
]

for card_info in card_list:
    print(card_info)







