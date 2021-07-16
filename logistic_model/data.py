from typing import Any, Tuple
import torch
import torch.nn as nn
import numpy as np
from torch.utils import data 
from torch.utils.data import Dataset 

class Mydata(Dataset):
    def __init__(self,file) -> None:
        self.file = file
        self.data = np.loadtxt(self.file)
        self.n,self.l = self.data.shape
        # super(Mydata).__init__()
    def get_train_test(self)->Tuple[np.ndarray,np.ndarray]:
        '返回训练数据的data和测试数据的data'
        for j in range(self.l-1):
            #归一化，如果一个batch做就是batch normalization
            meanVal = np.mean(self.data[:,j])#平均值
            stdVal = np.std(self.data[:,j])#标准差
            self.data[:,j]=(self.data[:,j]-meanVal)/stdVal
        #分离训练data和label
        np.random.shuffle(self.data)
        return self.data[:900,:],self.data[900:,:]
class Tensor_data(Dataset):
    def __init__(self,data) -> None:
        self.data = data
        # super(Tensor_data).__init__()
    def __len__(self)->Any:
        return len(self.data)
    def __getitem__(self, index) -> Tuple[Any,Any]:
        L = len(self.data[0]-1)
        train_data = self.data[:,:L-1]
        train_label = self.data[:,L-1:]-1
        train_data = torch.from_numpy(train_data).float()
        train_label = torch.from_numpy(train_label).long()
        return train_data[index],train_label[index]
file = './logistic_model/german.data-numeric'
train_data,valiad_data = Mydata(file=file).get_train_test()
train_data = Tensor_data(train_data)
valiad_data = Tensor_data(valiad_data)
# print(train_data)
# print(train_data[0])
# data = np.loadtxt('./logistic_model/german.data-numeric')
# n,l = data.shape
# print(n,l)
# print(data)
# np.random.shuffle(data)#打乱数据