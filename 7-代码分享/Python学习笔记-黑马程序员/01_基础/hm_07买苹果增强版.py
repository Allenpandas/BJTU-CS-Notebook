# 1.输入苹果的单价
price_str = input("苹果的单价为:")

# 2.输入苹果的重量
weight_str = input("apple weight:")

# 3.total
# [notice] 两个字符串变量之间不能直接用乘法,得强制类型转换
# money = price_str * weight_str

# 3.1价格换成小数
price = float(price_str)

# 3.2重量换成小数
weight = float(weight_str)

# 3.3求总价
money = price * weight

print(money)

