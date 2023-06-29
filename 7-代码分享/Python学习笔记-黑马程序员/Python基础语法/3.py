# names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
#
# a = [name.upper() for name in names]
# print(a)
#
# b = [name.upper() for name in names if len(name) > 3]
# print(b)



# names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
# dict = {key: len(key) for key in names} # 计算每个名字长度，名字做key，长度做value
# print(dict)


# set1 = {i**2 for i in (1, 2, 3)}
# print(set1)


a = (x for x in range(1,10))
print(a)

a = tuple(a)  # 使用tuple函数将元组生成器变成元组
print(a)
