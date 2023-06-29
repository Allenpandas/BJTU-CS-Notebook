# 第一遍
# name_list = ["a", "b", "e", "f", "g"]
# # 取值
# print(name_list[0])
# print(name_list[2])
# # 取索引
# print(name_list.index("e"))
# # 修改列表指定位置数据
# name_list[1] = "haha"
# print(name_list)
# # 追加元素
# name_list.append("aaa")
# print(name_list)
# # 任意位置插入
# name_list.insert(0,"helloworld")
# print(name_list)
# # 扩充列表
# list2 = ["孙悟空", "猪八戒"]
# name_list.extend(list2)
# print(name_list)
# # 删除,指定元素删除
# name_list.remove("helloworld")
# print(name_list)
# # 删除,pop弹出
# name_list.pop()
# print(name_list)
# # 删除,pop弹出,指定位置弹出
# name_list.pop(1)
# print(name_list)
# # 删除 清空
# name_list.clear()
# print(name_list)
##############################################
# 第二遍

# name_list = ["hello", "world", "Chinese", "America"]
# # 取值
# print(name_list[0])
# print(name_list[2])
# # 取索引
# print(name_list.index("America"))
# # 修改列表指定位置数据
# name_list[2] = "RPC"
# print(name_list)
# # 追加元素
# name_list.append("hahaha")
# print(name_list)
# # 任意位置插入
# name_list.insert(0,"NB")
# print(name_list)
# # 扩充列表
# tmp_list = ["aaa", "bbb", "ccc"]
# name_list.extend(tmp_list)
# print(name_list)
# # 删除,指定元素删除
# name_list.remove("aaa")
# print(name_list)
# # 删除,pop弹出
# name_list.pop()
# print(name_list)
# # 删除,pop弹出,指定位置弹出
# name_list.pop(2)
# print(name_list)
# # 删除 清空
# name_list.clear()
# print(name_list)

#################################################
name_list = ["a", "b", "c", "d"]
# 取值
print(name_list[0])
# 取索引
print(name_list.index("c"))
# # 修改列表指定位置数据
name_list[2] = "cc"
print(name_list)
# # 追加元素
name_list.append("e")
print(name_list)
# # 任意位置插入
name_list.insert(0,"aaa")
# # 扩充列表
name_tmp = ["aaa","bbb"]
name_list.extend(name_tmp)
print(name_list)
# # 删除,指定元素删除
name_list.remove("a")
print(name_list)
# # 删除,pop弹出
name_list.pop()
print(name_list)
# # 删除,pop弹出,指定位置弹出
name_list.pop(0)
print(name_list)

# # 删除 清空
name_list.clear()
print(name_list)
