# 定义字符串变量 name 输出 我的名字叫小明， 请多多关照
name = "大明"
print("我的名字叫：%s，请多多关照!" % name)

# 定义整型变量，student_no 输出我的学号是000001
student_no = 1
print("我的学号是%06d" % student_no)

# 定义小数 price`weight`money
price = 8.5
weight = 7.5
money = price * weight
print("苹果单价 %.2f 元/斤，购买了 %.2f 斤， 需要支付 %.2f 元" %(price, weight, money))

# 定义一个小数scale 输出 数据的比例是10.00%
scale = 0.25
print("数据的比例是 %.2f%%" % (scale * 100))