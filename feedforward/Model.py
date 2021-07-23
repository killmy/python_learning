import torch.nn as nn

#fully connect net:
class Simple_NeuraNet(nn.Module):
    def __init__(self,params):
        super(Simple_NeuraNet,self).__init__()
        self.fc1 = nn.Linear(params[0][0],params[0][1])
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(params[1][0],params[1][1])
    def forward(self,x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out