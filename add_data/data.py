import io
from typing import Any, Tuple
import torch
from torch import tensor 
import torch.nn as nn
import pandas as pd
from torch.utils.data import Dataset
from skimage import io,transform
import matplotlib.pyplot as plt
import numpy as np
path = "./add_data/faces/"
class Read_data(Dataset):
    def __init__(self) -> None:
        super().__init__()
        self.path = "./add_data/faces/"
        self.df = pd.read_csv("./add_data/faces/face_landmarks.csv")
    def __len__(self):
        return len(self.df)
    def __getitem__(self, index) -> Tuple[Any,Any]:
        length,data_dim = self.df.shape
        image = self.df.iloc[:,0]
        image = plt.imread(self.path+image[index])
        image = image/255
        image = image.astype(np.float)
        image = torch.tensor(image)
        landmaeks = self.df.iloc[index,1:]
        landmaeks = [x for x in landmaeks]
        landmaeks = torch.tensor(landmaeks).reshape(-1,2)
        return image,landmaeks

df = Read_data()
image,label = df[0]
print(image,label)
# image =plt.imread(path+image)
# image = image/255
# image = image.astype(np.float)
# print(type(image))
# plt.figure("show")
# plt.imshow(image)
# plt.show()
# df = pd.read_csv("./add_data/faces/face_landmarks.csv")
# # print(df.shape)
# # print(df.iloc[0,0])
# # print(type(df))

# # print(len(df))
# # print(df.loc[0]) #取索引为'0'的所有行
# # print(df.iloc[0])#取第0行
# # print(df.loc[:,'image_name']) #取image name这一列
# # print(df.iloc[:,0])
# length,data_dim = df.shape
# print(length,data_dim)
# image = df.iloc[:,0]
# print(type(image[0]))
# landmaeks = df.iloc[0,1:]
# landmaeks = landmaeks.astype('float')
# landmaeks = [x for x in landmaeks]
# print(landmaeks)
# landmaeks = torch.tensor(landmaeks).reshape(-1,2)
# print(landmaeks)
# print(landmaeks[0])
# print(type(landmaeks),landmaeks.shape)
'''
pandas 读取的数据类型分布
    A   B   C   D
a   0   1   2   3
b   4   5   6   7
c   8   9  10  11
d  12  13  14  15

'''