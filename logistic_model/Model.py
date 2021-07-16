import torch 
import numpy as np
import torch.nn as nn
from torch.nn.modules import linear

#二分类，此处数据没有用V表示输出,所以要自己加上
class Logistic_Model(nn.Module):
    def __init__(self):
        super(Logistic_Model,self).__init__()
        self.fc = nn.Linear(24,2)
    def forward(self,x):
        out = self.fc(x)
        #交叉熵自带sigmoid所以不需要加上sigmoid
        return out