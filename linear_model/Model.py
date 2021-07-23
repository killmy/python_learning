import torch
import torch.nn as nn

class Linear_Model(nn.Module):
    def __init__(self):
        super(Linear_Model,self).__init__()
        self.fc = nn.Linear(1,1)
    def forward(self,x):
        out = self.fc(x)
        return out