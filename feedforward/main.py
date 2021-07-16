import torch
from torch._C import device
from torch.autograd.grad_mode import no_grad
import torch.nn as nn
from torch.nn.modules import loss
from torch.utils import data
from torch.utils.data.dataset import Dataset
import torchvision
import torchvision.transforms as tranforms
from torch.utils.data import DataLoader
import Model
# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Hyper-parameters 
class Hyper_parameters():
    def __init__(self) -> None:
        #net paramers
        self.params_fc1 = [1*28*28,500]
        self.params_fc2 = [500,10]  
        self.params = [self.params_fc1,self.params_fc2]
        self.batch_size = 100
        self.num_classes = 10
        self.num_epochs = 5
        self.learn_rate = 0.001
params = Hyper_parameters()

#data
#download 
train_data = torchvision.datasets.MNIST(root="./feedforward/data",
                                                                 train=True,
                                                                 transform=tranforms.ToTensor(),
                                                                 download=True)
test_data = torchvision.datasets.MNIST(root="./feedforward/data",
                                                                 train=False,
                                                                 transform=tranforms.ToTensor(),
                                                                 download=True)
# image,label = train_data[0]
# print(image.size())
#shufft and transform 
train_loader = DataLoader(dataset=train_data,
                                            batch_size=params.batch_size,
                                            shuffle=True)
test_loader = DataLoader(dataset=test_data,
                                            batch_size=params.batch_size,
                                            shuffle=False)
                                                           
model = Model.Simple_NeuraNet(params=params.params).to(device=device)

#Loss and optimizer
cirterion  = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),lr=params.learn_rate)

#train 
total_step = len(train_data)
for epoch in range(params.num_epochs):
    for i ,(images,labels) in enumerate(train_loader):
        images = images.reshape(-1,28*28).to(device)
        labels = labels.to(device)

        #forward 
        outputs = model(images)
        loss = cirterion(outputs,labels)

        #backward
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (i+1)%params.batch_size == 0:
            print("Epcho [{}/{}],step [{}/{}],loss:{:.4f}".format(epoch+1,params.num_epochs,i+1,total_step,loss.item()))

#test
with torch.no_grad():
    correct = 0
    total = 0
    for images,labels in test_loader:
        images = images.reshape(-1,28*28).to(device)
        labels = labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0) #总的
        correct += (predicted == labels).sum().item()
    print('Accuracy of the network on the 10000 test images: {} %'.format(100 * correct / total))

# Save the model checkpoint
torch.save(model.state_dict(), './feedforward/param.ckpt')