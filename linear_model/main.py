from numpy.core.numeric import outer
import torch
import numpy as np
from torch.nn.modules import loss
from torch.optim import optimizer 
import data
import Model
import torch.nn as nn
import matplotlib.pyplot as plt
if torch.cuda.is_available():
    print(torch.cuda.current_device())
    device = torch.device('cuda')
#params
class Data_Params():
    def __init__(self) -> None:
        self.train_data = data.read_data()
        self.batch_size = len(self.train_data)
        self.train_loader = torch.utils.data.DataLoader(dataset=self.train_data,
                                           batch_size=self.batch_size, 
                                           shuffle=True)
        self.learning_rate = 0.001
        self.epochs = 60
params = Data_Params()
model = Model.Linear_Model()
#model = nn.Linear(1,1)
#loss and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(),lr=params.learning_rate)

# Train the model
for epoch in range(params.epochs):
    for i, (images, labels) in enumerate(params.train_loader):
        #forward pass
        outputs = model.forward(images)
        loss = criterion(outputs,labels)

        #backward
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    if (epoch+1) % 5 == 0:
        print ('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, params.epochs, loss.item()))

torch.save(model,'./linear_model/model.ckpt')
torch.save(model.state_dict(),'./linear_model/params.ckpt')

for i, (images, labels) in enumerate(params.train_loader):
    #forward pass
    pred = model.forward(images)
    images = images.numpy()
    labels = labels.numpy()
    pred = pred.detach().numpy()
    plt.plot(images,labels,'r--o',label='traget')
    plt.plot(images,pred,'b--o',label="pred")
    plt.legend()
    plt.show()
    