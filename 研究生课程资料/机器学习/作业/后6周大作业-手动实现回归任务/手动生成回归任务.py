# 手动实现前馈神经网络解决回归问题
import torch
import matplotlib.pyplot as plt
import numpy as np


# 定义模型
def net(X, w, b):
    return torch.matmul(X, w) + b


# 定义损失函数：MSELoss  1/2 * (y_pred - y)²
def MSELoss(y_hat, y):
    return (y_hat - y) ** 2 / 2


# 梯度下降
def sgd(params, lr, batch_size):
    for param in params:
        param.data -= lr * param.grad / batch_size


# 计算模型在某个数据集上的准确率
def cal_loss(data_iter, w, b, net, loss):
    acc_sum, n = 0.0, 0
    for X, y in data_iter:
        l = loss(net(X, w, b), y).sum()
        acc_sum += l.item()
        n += y.shape[0]
    return acc_sum / n


# 定义训练模型
def train(epochs, train_iter, test_iter, w, b, batch_size, lr, loss):
    train_loss = []
    test_loss = []
    params = [w, b]
    for epoch in range(epochs):  # 外层循环控制循环轮次
        for X, y in train_iter:  # 内层循环控制循环批次
            y_hat = net(X, w, b)
            l = loss(y_hat, y).sum()
            if w.grad is not None:
                for param in params:
                    param.grad.data.zero_()
            l.backward()  # 反向传播
            sgd(params, lr, batch_size)  # 默认采用SGD函数

        # 记录训练集和测试机的准确率
        train_l = cal_loss(train_iter, w, b, net, loss)
        test_l = cal_loss(test_iter, w, b, net, loss)
        train_loss.append(train_l)
        test_loss.append(test_l)
        print('epoch %d, train loss %.6f, test loss %.6f, w %.6f, b %.6f'
              % (epoch + 1, train_l, test_l, w.mean().item(), b.mean().item()))

    return train_loss, test_loss


# 数据集的样本特征维度p为500
num_inputs = 500
# 真实 w b
true_w = torch.ones(num_inputs, 1) * 0.0056
true_b = 0.028
# 训练样本数
train_num = 7000
# 测试样本数
test_num = 3000
# 随机批量数
batch_size = 512
# 训练次数
epochs = 30
# 学习率
lr = 0.01
# 损失函数
loss = MSELoss
# w b 初始化
w = torch.normal(0, 0.1, (num_inputs, 1), dtype=torch.float32, requires_grad=True)
b = torch.zeros(1, dtype=torch.float32, requires_grad=True)

# 样本生成
features = torch.randn((train_num + test_num), num_inputs)
labels = torch.mm(features, true_w) + true_b
labels += torch.tensor(np.random.normal(0, 0.01, size=labels.size()))
train_features, test_features = features[:train_num, :], features[train_num:, :]
train_labels, test_labels = labels[:train_num], labels[train_num:]

train_dataset = torch.utils.data.TensorDataset(train_features, train_labels)
test_dataset = torch.utils.data.TensorDataset(test_features, test_labels)

train_iter = torch.utils.data.DataLoader(train_dataset, batch_size, shuffle=True)
test_iter = torch.utils.data.DataLoader(test_dataset, batch_size, shuffle=False)

# 开始训练
train_loss, test_loss = train(epochs, train_iter, test_iter, w, b, batch_size, lr, loss)

# 绘图
x = np.linspace(0, len(train_loss), len(train_loss))
plt.plot(x, train_loss, label="train_loss", linewidth=1.5)
plt.plot(x, test_loss, label="test_loss", linewidth=1.5)
plt.xlabel("epoch")
plt.ylabel("loss")
plt.legend()
plt.savefig('/Users/wuyalun/Desktop/1-1.jpg')
plt.show()
