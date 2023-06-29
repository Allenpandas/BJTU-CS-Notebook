import numpy as np


def f(x):
    return x ** 2


def h(x):
    return 2 * x


x = 2  # 初始点（初始横坐标）
step = 0.8  # （步长）

f_change = f(x)
f_current = f(x)
count = 0  # 迭代次数
while f_change > 1e-10:  # 停止迭代的条件，差值小于10^-10的时候停止迭代

    x = x - step * h(x)  # 更新x
    tmp = f(x)  # 更新x之后的f(x)的值，用另一个变量接收
    f_change = np.abs(f_current - tmp)  # x更新前后的y的差值
    f_current = tmp  # 将更新的f(x)传入下一次的迭代
    count += 1  # 增加一次迭代次数

print('迭代了：%d次' % count, '\n''求得x为：', x, '\n''求得y为：', f_current)
