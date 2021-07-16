# from numpy.core.numeric import outer
# from torch import optim
# from torch.nn.modules import loss
# import data
# import torch 
# import torch.nn as nn
# import Model
# batch_size = 100
# lr = 0.001
# num_epochs = 5
# file = './logistic_model/german.data-numeric'
# train_data,valiad_data = data.Mydata(file=file).get_train_test()
# train_data = data.Tensor_data(train_data)
# valiad_data = data.Tensor_data(valiad_data)
# train_loader = torch.utils.data.DataLoader(dataset=train_data, 
#                                            batch_size=batch_size, 
#                                            shuffle=True)

# test_loader = torch.utils.data.DataLoader(dataset=valiad_data, 
#                                           batch_size=batch_size, 
#                                           shuffle=False)
# model = Model.Logistic_Model()

# # Loss and optimizer
# # nn.CrossEntropyLoss() computes softmax internally    
# criterion = nn.CrossEntropyLoss()
# optimizer = torch.optim.SGD(model.parameters(), lr=lr)  
# print(len(train_loader))
# # Train the model
# total_step = len(train_loader)
# for epoch in range(num_epochs):
#     for i,(traindatas,labels) in enumerate(train_data):
#         #forward
#         #outputs = model.forward(traindatas)
#         print(labels)
#         #loss = criterion(outputs,labels)

#         # #backward
#         # optimizer.zero_grad()
#         # loss.backward()
#         # optimizer.step()

#         # if (i+1)%batch_size==0:
#         #     print ('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}' 
#         #            .format(epoch+1, num_epochs, i+1, total_step, loss.item()))
# Test the model
# In test phase, we don't need to compute gradients (for memory efficiency)
# with torch.no_grad():
#     correct = 0
#     total = 0
#     for images, labels in test_loader:
#         images = images.reshape(-1, input_size)
#         outputs = model(images)
#         _, predicted = torch.max(outputs.data, 1)
#         total += labels.size(0)
#         correct += (predicted == labels).sum()

#     print('Accuracy of the model on the 10000 test images: {} %'.format(100 * correct / total))

# # Save the model checkpoint
# torch.save(model.state_dict(), 'model.ckpt')