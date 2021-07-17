from numpy.core.defchararray import mod, title
import torch
from torch.autograd.grad_mode import no_grad
from torch.functional import Tensor 
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
import Moedl
from tensorboardX import SummaryWriter

logger = SummaryWriter(log_dir="./CNN/log")
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
        global_iter_num  = epoch*total_step+i+1
        if (i+1)%params.batch_size==0:
            print('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}' 
            .format(epoch+1, params.num_epochs, i+1, total_step, loss.item()))
            logger.add_scalar("train loss", loss.item() ,global_step=global_iter_num)#https://blog.csdn.net/u012343179/article/details/83007296
            #拼接mini-batch
            img = torchvision.utils.make_grid(images,nrow=12) 
            print(img.size())
            logger.add_image("train image sample", img, global_step=global_iter_num)
            # writer.add_image("train_image_sample",img,global_step=global_iter_num)
            model = model.cpu()
            for name ,param in model.named_parameters():
                #https://blog.csdn.net/moshiyaofei/article/details/90519430
                #要先转化为cpu才能转化为numpy
                logger.add_histogram("param", param.data.numpy(), global_step=global_iter_num)
            model = model.cuda()
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
