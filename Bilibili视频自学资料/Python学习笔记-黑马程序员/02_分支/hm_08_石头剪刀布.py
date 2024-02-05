import random

player = int(input("请输入您要出的拳 石头（1）/ 剪刀（2）/ 布（3）\n"))

computer = random.randint(1,3)

print("玩家出的拳头是 %d - 电脑出的拳头是 %d " %(player, computer))

# 石头1 胜 剪刀2
# 剪刀2 胜 布3
# 布3   胜 石头1
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("赢了，电脑弱爆了")
elif (player == computer):
    print("平局，真是心有灵犀啊")
else:
    print("你输了，电脑毕竟是电脑")
