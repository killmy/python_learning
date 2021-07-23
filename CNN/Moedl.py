'''
coding:utf-8
网站:https://github.com/yunjey/pytorch-tutorial/blob/master/tutorials/02-intermediate/convolutional_neural_network/main.py#L35-L56
https://zhuanlan.zhihu.com/p/220403674
'''
from re import X
import torch
import torch.nn as nn
import hiddenlayer as h
from torch.nn.modules.batchnorm import BatchNorm2d
from torchviz import make_dot
# 在cnn中一张图片看成一个数据
class MNIST_CNNModel(nn.Module):
    def __init__(self,num_classes=10):
        super(MNIST_CNNModel,self).__init__()
        self.layer1 = nn.Sequential(
            #(image.size+2*padding-kernel_size)+stride
            nn.Conv2d(1,16,kernel_size=5,stride=1,padding=2),
            #对应通道对应数据做，Batch_sizexWxH
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2,stride=2))
        self.layer2 = nn.Sequential(
            nn.Conv2d(16,32,kernel_size=5,stride=1,padding=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2,stride=2)
        )
        self.fc = nn.Linear(7*7*32,num_classes)
    def forward(self,x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = out.reshape(out.size(0),-1)
        out = self.fc(out)
        return out

# model = MNIST_CNNModel(10)
# image = torch.randn(1,1,28,28,requires_grad=True)
# y = model(image)
# print(image.size())
# # MyConvNetVis = make_dot(y, params=dict(list(model.named_parameters()) + [('x', image)]))
# # MyConvNetVis.format = "png"
# # MyConvNetVis.directory = "E:/python_learning/CNN"
# # MyConvNetVis.view()

# # 这里包含了batch_size这一个维度
# vis_grap = h.build_graph(model,image)
# vis_grap.theme = h.graph.THEMES['blue'].copy()
# vis_grap.save("E:/python_learning/CNN/Moedl.png")

