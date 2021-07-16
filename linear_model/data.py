from typing import Any, Tuple
import torch
import numpy as np
import matplotlib.pyplot as plt
from torch.utils import data
from torch.utils.data import Dataset

#创建数据
x_train = np.array([[3.3], [4.4], [5.5], [6.71], [6.93], [4.168], 
                    [9.779], [6.182], [7.59], [2.167], [7.042], 
                    [10.791], [5.313], [7.997], [3.1]], dtype=np.float32)

y_train = np.array([[1.7], [2.76], [2.09], [3.19], [1.694], [1.573], 
                    [3.366], [2.596], [2.53], [1.221], [2.827], 
                    [3.465], [1.65], [2.904], [1.3]], dtype=np.float32)

#输入的数据都是vector，加上batch的[]
class Train_data(Dataset):
    def __init__(self,x_train,y_train) -> None:
        self.x_train = torch.from_numpy(x_train)
        self.y_train = torch.from_numpy(y_train)
    def __len__(self):
        return len(self.x_train)
    def __getitem__(self, index) -> Tuple[Any,Any]:
        return self.x_train[index],self.y_train[index]
def read_data()->Tuple[Any,Any]:
    data = Train_data(x_train=x_train,y_train=y_train)
    return data

# data = Train_data(x_train,y_train)
# x_train,y_train=data[0]
# print(x_train,y_train)
# batch_size = len(data)

# train_data = read_data()
# batch_size = len(train_data)
# train_loader = torch.utils.data.DataLoader(dataset=train_data,
#                                            batch_size=batch_size, 
#                                            shuffle=True)
# for i, (images, labels) in enumerate(train_loader):
#     print(images,labels)