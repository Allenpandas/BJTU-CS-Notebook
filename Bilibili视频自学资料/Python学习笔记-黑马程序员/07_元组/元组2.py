info_tuple = ("zhangsan", 18, "178cm", 18)

# 取值和取索引
print(info_tuple[0])
# 输出：zhangsan

# 取索引(已经知道内容，获取位置)
print(info_tuple.index("178cm"))
# 输出：2 输出178cm在元组中的索引的值

# 统计计数
print(info_tuple.count(18))
print(info_tuple.count("178cm"))

# 包含元素个数
print(len(info_tuple))