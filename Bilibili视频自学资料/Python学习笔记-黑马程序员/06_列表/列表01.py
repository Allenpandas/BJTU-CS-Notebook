# 列表的常用操作
name_list = ["吴亚伦", "高远哲", "王兴辉", "翟宪伟"]
# print(name_list)

# 取值
# name_list[]
# print(name_list[0])
# print(name_list[2])

# 取索引
# name_list.index()
# print(name_list.index("翟宪伟"))

# 修改列表指定位置数据
# name_list[1] = "gaoyuanzhe"
# name_list[4] = 'aaa' # 索引超出范围，会报错，不会进行赋值操作
# print(name_list)


# 追加元素
# append 末尾追加元素
# name_list.append("许振业")
# print(name_list)

# insert 任意位置插入,原数据往后排
# name_list.insert(1,"许振业")
# print(name_list)

# extend 其他list[]的数据追加到原list列表中
# tmp_list = ["孙悟空", "猪八戒"]
# name_list.extend(tmp_list)
# print(name_list)

# 删除
# remove 删除指定元素
# name_list.remove("吴亚伦")
# print(name_list)

# pop 弹出(指定位置弹出)
# name_list.pop()  # 默认弹出最后一个
# print(name_list)
# name_list.pop(1)    # 支持弹出指定元素
# print(name_list)

# clear 清空整个列表
name_list.clear()
print(name_list)

# del 关键词删除(了解即可，不建议使用)
# del name_list[1]

# print(name_list)