#coding:utf-8
#用途：学习pytorch
#参考链接：https://github.com/yunjey/pytorch-tutorial/blob/master/tutorials/01-basics/pytorch_basics/main.py
#参考链接1：https://github.com/zergtant/pytorch-handbook/blob/master/chapter1/2_autograd_tutorial.ipynb
#pytorch手册：https://pytorch-cn.readthedocs.io/zh/latest/
from typing import Any
from cffi import model
from numpy.lib.type_check import imag
import torch
import numpy as np
from torch._C import device
import torch.nn as nn
from torch.utils.data import Dataset
from torch.nn.modules import loss
from torch.nn.modules.transformer import Transformer
import torchvision
import torchvision.transforms as transform
from torchvision.transforms import transforms
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import pandas as pd
#Use GPU.好像默认使用GPU
if torch.cuda.is_available():
    print(torch.cuda.current_device())
    device = torch.device('cuda')
'''
Contents:
1. Basic autograd example1
2. Basic autograd example2
3. loading data from numpy
'''
#=============================#
# Basic autograd example1                               #
#=============================#
#create tensors.
#'requires_grad=True' open autograd or 'x.requires_grad_(True)'
#每个张量都有一个.grad_fn属性，这个属性引用了一个创建了Tensor的Function
x = torch.tensor(1.,requires_grad=True)
w = torch.tensor(3.,requires_grad=True)
b = torch.tensor(2.,requires_grad=True)

#Function.Build a computational graph.
y = w*x+b

#Compute gradients.
y.backward()

#Print out the gradients,tensor type
#tensor-->numpy
print(x.grad.numpy())   #x.grad = 3.
print(w.grad)   #w.grad =1. 
print(b.grad)   #b.grad = 1.

#=============================#
# Basic autograd example2                               #
#=============================#
#Create tensors
#input x 
x = torch.randn(10,3)#10个数据每个数据三个属性x1,x2,x3
#output y
y = torch.rand(10,2)#10个数据，每个数据2个属性
x.to(device)
y.to(device)
#Build a fully connected layer
#得到参数的方法
linear = nn.Linear(3,2)#创建W和b. W：3x2.b:2x1
print('w: ',linear.weight)
print('b',linear.bias)
for param in linear.parameters():
    print(param)

#Build loss function and optimizer.
criterion = nn.MSELoss() #使用均方差
optimizer = torch.optim.SGD(linear.parameters(),lr=0.01) #lr 学习率

#Forward pass
pred = linear(x)

#Computer loss
loss = criterion(pred,y)
print('loss: ',loss)

#Backward loss
loss.backward()

#print out the gradients.
print('dL/dw: ',linear.weight.grad)
print('dL/db: ',linear.bias.grad)

#one-step gradient descent
optimizer.step()

# You can also perform gradient descent at the low level.
# linear.weight.data.sub_(0.01 * linear.weight.grad.data)
# linear.bias.data.sub_(0.01 * linear.bias.grad.data)

pred = linear(x)
loss = criterion(pred,y)
print('loss after 1 step optimization: ', loss.item())

#=============================#
# Loading data from numpy                          #
#=============================#
# Creat a numpy array
x = np.array([[1,2],[3,4]])

#numpy-->tensor
y = torch.from_numpy(x)

#tensor-->numpy
z = y.numpy()

#=============================#
# Input in-place pipeline                                   #
#=============================#
# Download and construct CIRAR-10 dataset.
train_dataset = torchvision.datasets.CIFAR10(root='./quick_in/data',
                                             train=True, 
                                             transform=transforms.ToTensor(),
                                             download=True)

# Fetch one data pair (read data from disk).
image,label = train_dataset[0]
print(image.size())
print(label)

# Data loader (this provides queues and threads in a very simple way).
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                           batch_size=64, 
                                           shuffle=True)

# When iteration starts, queue and thread start to load data from files.
data_iter = iter(train_loader)#取一个batch

# Mini-batch images and labels.
images, labels = data_iter.next()
print(images[0])
print(labels.size())

#show image
#使用matplotlib
img = images[0]
img = img.numpy()
img = np.transpose(img, (1,2,0)) #0，1，2代表维,3x32x32-->32x32x3
plt.imshow(img)
plt.show()
#使用opencv2
#缩放到0~256
maxValue = img.max()
img = img*255/maxValue
img = np.uint8(img)
print(img)
cv2.imshow('img',img)
cv2.waitKey(0)
# Actual usage of the data loader is as below.
for images, labels in train_loader:
    # Training code should be written here.
    pass

#=============================#
# Input pipeline for custom dataset                  #
#=========================++====#
# You should build your custom dataset as below.
class CustomDataset(Dataset):
    def __init__(self,csv_file) -> None:
        # do:
        # 1. Initialize file paths or a list of file names. 
        # as
        self.df = pd.read_csv(csv_file)
        super().__init__()#继承父类的一些参数
    def __len__(self):
        # You should change 0 to the total size of your dataset.
        return len(self.df)
    def __getitem__(self, index) -> Any:
        # 1. Read one data from file (e.g. using numpy.fromfile, PIL.Image.open).
        # 2. Preprocess the data (e.g. torchvision.Transform).
        # 3. Return a data pair (e.g. image and label).
        return self.df.iloc[index].SalePrice #返回train_dataset
        #return super().__getitem__(index)
#=============================#
# Pretrained model                                           #
#=============================#
# Download and load the pretrained ResNet-18.
resnet = torchvision.models.resnet18(pretrained=True)

# If you want to finetune only the top layer of the model, set as below.
for param in resnet.parameters():
    param.requires_grad = False #不更新参数，可以用来固定模型，对抗网络get

# Replace the top layer for finetuning.替换顶层进行微调
print(resnet.fc.in_features,resnet.fc.out_features)
resnet.fc = nn.Linear(resnet.fc.in_features,100)

#Forward pass
images = torch.randn(64, 3, 224, 224)
outputs = resnet(images)
print (outputs.size())

#=============================#
# save and load model                                      #
#=============================#

#Save and load the entire model.
torch.save(resnet,'./model.ckpt')
model = torch.load('./model.ckpt')

# Save and load only the model parameters (recommended).
torch.save(resnet.state_dict(),'./params.ckpt')
resnet.load_state_dict(torch.load('./params.ckpt'))