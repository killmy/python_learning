from numpy.core.defchararray import mod, title
import torch
from torch.autograd.grad_mode import no_grad 
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
import Moedl
import tensorboard
# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Hyper parameters
# Hyper-parameters 
class Hyper_parameters():
    def __init__(self) -> None:
        #net paramers
        self.batch_size = 100
        self.num_classes = 10
        self.num_epochs = 5
        self.learn_rate = 0.001
params = Hyper_parameters()

# MNIST dataset
train_dataset = torchvision.datasets.MNIST(root='./CNN/data/',
                                           train=True, 
                                           transform=transforms.ToTensor(),
                                           download=True)

test_dataset = torchvision.datasets.MNIST(root='./CNN/data/',
                                          train=False, 
                                          transform=transforms.ToTensor())

# Data loader
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                           batch_size=params.batch_size, 
                                           shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                          batch_size=params.batch_size, 
                                          shuffle=False)

# Show part picture
# plt.figure("show")
# for i in range(6):
#     image,label = train_dataset[i]
#     print(image.size())
#     subplot_label = 23*10+i+1
#     print(subplot_label,type(subplot_label))
#     plt.subplot(subplot_label,title=str(label))
#     # plt.subplot(subplot_label,title=str(label))
#     image = image.numpy()
#     image = np.transpose(image,(1,2,0))
#     print(image.shape)
#     plt.imshow(image,cmap='gray')
# plt.show()

# model
model = Moedl.MNIST_CNNModel(params.num_classes).to(device)

#loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),lr=params.learn_rate)

#train
total_step = len(train_loader)
for epoch in range(params.num_epochs):
    for i,(images,labels) in enumerate(train_loader):
        images = images.to(device)
        labels = labels.to(device)

        #forward 
        outputs = model(images)
        loss = criterion(outputs,labels)

        #backward 
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        #show
        if (i+1)%params.batch_size==0:
            print('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}' 
            .format(epoch+1, params.num_epochs, i+1, total_step, loss.item()))

#test 
#固定batch normalization and dropout
model.eval() # eval mode (batchnorm uses moving mean/variance instead of mini-batch mean/variance)
with torch.no_grad():
    correct = 0
    total = 0
    for images,labels in test_loader:
        images = images.to(device)
        labels = labels.to(device)
        outputs = model(images)
        _,predicted = torch.max(outputs,1)
        total +=labels.size(0)
        print(labels.size(0))
        correct +=(predicted==labels).sum().item()
    

    print('Test Accuracy of the model on the 10000 test images: {} %'.format(100 * correct / total))

#save
torch.save(model.state_dict(),'./CNN/param.ckpt')
