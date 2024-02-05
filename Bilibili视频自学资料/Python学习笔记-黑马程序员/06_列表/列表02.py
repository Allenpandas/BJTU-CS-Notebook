# 列表的常用操作
name_list = ["吴亚伦", "高远哲", "王兴辉", "翟宪伟", "许振业", "翟宪伟", "翟宪伟"]
print(name_list)

# len计算元素个数
print(len(name_list))

# count 统计某个元素重复出现的次数
print(name_list.count("翟宪伟"))

# remove删除第一个出现的元素，即：3号位的翟宪伟
name_list.remove("翟宪伟")
print(name_list)


