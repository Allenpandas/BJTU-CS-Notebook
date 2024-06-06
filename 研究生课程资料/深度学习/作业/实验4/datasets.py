#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import torch
import torch.utils.data as data
import warnings
warnings.filterwarnings("ignore")


# 定义dataset
class my_Dataset(data.Dataset):
    def __init__(self, features, labels):
        self.X = features
        self.y = labels

    def __getitem__(self, index):
        return self.X[index], self.y[index]

    def __len__(self):
        return self.X.shape[0]


# 空气质量数据集
class KrakowDataset:
    def __init__(self, sensor=171, is_resample=True):
        # 选取几个月个月的数据
        self.month = ['april-2017', 'august-2017', 'december-2017', 'february-2017',
                      'january-2017', 'july-2017', 'june-2017', 'march-2017',
                      'may-2017', 'november-2017', 'october-2017', 'september-2017']
        raw_data = pd.concat([pd.read_csv(f'./dataset/Krakow-airquality/{month}.csv') for month in self.month])

        # 确定特征列
        features = ['temperature', 'humidity', 'pressure', 'pm1', 'pm25', 'pm10']
        self.sensor = sensor    # 选取探测器,并非每个探测器都有数据
        self.feature_col = ['UTC time'] + [f'{self.sensor}_{fea}' for fea in features]
        data_df = raw_data[[col for col in raw_data.columns if col in self.feature_col]]

        # 按时间戳排序
        data_df['UTC time'] = pd.to_datetime(data_df['UTC time'])
        data_df = data_df.set_index('UTC time').sort_index()

        # 重采样、插分
        if is_resample:
            self.start_time, self.end_time = data_df.index.min(), data_df.index.max()
            full_index = pd.date_range(self.start_time, self.end_time, freq='h')
            data_df = data_df.reindex(full_index)
            data_df = data_df.interpolate(method='linear')
        else:
            data_df = data_df.dropna()

        # 数据标准化
        self.min = data_df.min()
        self.max = data_df.max()
        self.data = (data_df - self.min) / (self.max - self.min)

    def denormalize(self, x):
        key = f'{self.sensor}_{self.target}'
        return x * (self.max[key] - self.min[key]) + self.min[key]

    def construct_set(self, train_por=0.6, test_por=0.2, window_size=12, target='pm25'):
        train_x = []
        train_y = []
        val_x = []
        val_y = []
        test_x = []
        test_y = []
        self.target = target
        self.feature_col.remove('UTC time')
        self.data = self.data.reset_index()

        len_train = int(self.data.shape[0] * train_por)
        train_seqs = self.data[:len_train]
        for i in range(train_seqs.shape[0] - window_size):
            train_seq = train_seqs.loc[i:i + window_size]
            train_x.append(train_seq.loc[i:i + window_size - 1][self.feature_col].values.tolist())
            train_y.append(train_seq.loc[i + window_size][f'{self.sensor}_{target}'].tolist())

        len_val = int(self.data.shape[0] * (train_por + test_por))
        val_seqs = self.data[len_train:len_val]
        val_seqs = val_seqs.reset_index()
        for i in range(val_seqs.shape[0] - window_size):
            val_seq = val_seqs.loc[i:i + window_size]
            val_x.append(val_seq.loc[i:i + window_size - 1][self.feature_col].values.tolist())
            val_y.append(val_seq.loc[i + window_size][f'{self.sensor}_{target}'].tolist())

        test_seqs = self.data[len_val:]
        test_seqs = test_seqs.reset_index()
        for i in range(test_seqs.shape[0] - window_size):
            test_seq = test_seqs.loc[i:i + window_size]
            test_x.append(test_seq.loc[i:i + window_size - 1][self.feature_col].values.tolist())
            test_y.append(test_seq.loc[i + window_size][f'{self.sensor}_{target}'].tolist())

        train_set = my_Dataset(torch.Tensor(train_x), torch.Tensor(train_y))
        val_set = my_Dataset(torch.Tensor(val_x), torch.Tensor(val_y))
        test_set = my_Dataset(torch.Tensor(test_x), torch.Tensor(test_y))
        return train_set, val_set, test_set


class TrafficDataset:
    def __init__(self, sensor=10, target=0):
        # 选取适当的检测器用作序列数据
        self.raw_data = np.load('./dataset/traffic-flow/traffic.npz')['data']
        self.sensor = sensor
        self.target = target
        # 数据标准化
        self.min = self.raw_data.min()
        self.max = self.raw_data.max()
        self.data = (self.raw_data - self.min) / (self.max - self.min)

    def denormalize(self, x):
        return x * (self.max - self.min) + self.min

    def construct_set(self, train_por=0.6, test_por=0.2, window_size=12, label=0):
        train_x = []
        train_y = []
        val_x = []
        val_y = []
        test_x = []
        test_y = []


        len_train = int(self.data.shape[0] * train_por)
        train_seqs = self.data[:len_train]
        for i in range(train_seqs.shape[0] - window_size):
            train_x.append(train_seqs[i:i+window_size, self.sensor, :].squeeze())
            train_y.append(train_seqs[i+window_size, self.sensor, self.target].squeeze())

        len_val = int(self.data.shape[0] * (train_por + test_por))
        val_seqs = self.data[len_train:len_val]
        for i in range(val_seqs.shape[0] - window_size):
            val_x.append(val_seqs[i:i+window_size, self.sensor, :].squeeze())
            val_y.append(val_seqs[i+window_size, self.sensor, self.target].squeeze())

        test_seqs = self.data[len_val:]
        for i in range(test_seqs.shape[0] - window_size):
            test_x.append(test_seqs[i:i+window_size, self.sensor, :].squeeze())
            test_y.append(test_seqs[i+window_size, self.sensor, self.target].squeeze())

        train_set = my_Dataset(torch.Tensor(train_x), torch.Tensor(train_y))
        val_set = my_Dataset(torch.Tensor(val_x), torch.Tensor(val_y))
        test_set = my_Dataset(torch.Tensor(test_x), torch.Tensor(test_y))
        return train_set, val_set, test_set


class FourSquareDataset:
    def __init__(self, data_path):
        # 适当修改数据读取过程
        self.raw_data = pd.read_csv(data_path)
        self.min = self.raw_data.min()
        self.max = self.raw_data.max()
        self.data = (self.raw_data - self.min) / (self.max - self.min)

    def denormalize(self, x, feat):
        return x * (self.max - self.min) + self.min

    def construct_set(self, train_por, test_por, window_size, label=0):
        train_x = []
        train_y = []
        val_x = []
        val_y = []
        test_x = []
        test_y = []

        # 补全构造过程
        pass

        train_set = my_Dataset(torch.Tensor(train_x), torch.Tensor(train_y))
        val_set = my_Dataset(torch.Tensor(val_x), torch.Tensor(val_y))
        test_set = my_Dataset(torch.Tensor(test_x), torch.Tensor(test_y))
        return train_set, val_set, test_set


# In[ ]:



