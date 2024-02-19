import torch
import torch.nn as nn
import torch.utils.data
import torch.nn.init
import numpy as np
from matplotlib import pyplot as plt

n_train = 7000
n_test = 3000
num_inputs = 500
true_w = torch.ones(num_inputs, 1) * 0.0056
true_b = 0.028

features = torch.randn(n_train + n_test, num_inputs)
labels = torch.matmul(features, true_w) + true_b


# labels += torch.tensor(np.random.normal(0, 0.01, size=labels.size()),dtype=torch.float);
train_features = features[ : n_train, :]
test_features = features[n_train: , :]
train_labels = labels[ : n_train]
test_labels = labels[n_train : ]

# 添加一次性读取数据量
batch_size = 200
# epochs迭代次数
num_epochs = 15
# 学习率
lr = 0.03

dataset = torch.utils.data.TensorDataset(train_features, train_labels)
train_iter = torch.utils.data.DataLoader(dataset, batch_size, shuffle=True)

dataset = torch.utils.data.TensorDataset(test_features, test_labels)
test_iter = torch.utils.data.DataLoader(dataset, batch_size, shuffle=False)


# MSE损失函数
def loss(y_hat, y):
    return (y_hat - y.view(y_hat.size())) ** 2 / 2


def train():
    net = nn.Linear(num_inputs, 1)
    nn.init.normal_(net.weight, mean=0, std=1)
    nn.init.normal_(net.bias, mean=0, std=1)
    optimizer_w = torch.optim.SGD(params=[net.weight], lr=lr)
    optimizer_b = torch.optim.SGD(params=[net.bias], lr=lr)
    train_ls = []
    test_ls = []

    n, train_loss_sum = 0, 0
    n_test, test_loss_sum = 0, 0

    for epoch in range(num_epochs):
        for X, y in train_iter:
            l = loss(net(X), y).mean()
            optimizer_b.zero_grad()
            optimizer_w.zero_grad()
            l.backward()
            optimizer_w.step()
            optimizer_b.step()
            train_loss_sum += l.item()
            n += y.shape[0]
        train_ls.append(train_loss_sum / n)

        for X, y in test_iter:
            l = loss(net(X), y)
            l = l.sum()
            n_test += y.shape[0]
            test_loss_sum += l.item()
        test_ls.append(test_loss_sum / n)
        print('epoch %d, w= %.4f, b= %.3f' % (epoch + 1, net.weight.mean().item(), net.bias.mean().item()))

    x = np.linspace(0, len(train_ls), len(train_ls))
    plt.plot(x, train_ls, label="train_loss", linewidth=2)
    plt.plot(x, test_ls, label="test_loss", linewidth=1.5)
    plt.xlabel("epoch")
    plt.ylabel("loss")
    plt.legend()
    plt.savefig('/Users/wuyalun/Desktop/2-1.jpg')
    plt.show()

train()


