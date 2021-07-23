### MNIST 手写字体的识别
1. hidden layer
卷积->batch normal->relu->下采样
2. reshape
3. fully connect->num_classess 

交叉熵自带softmax

### torch.max()
output = torch.max(input, dim)  
input是softmax函数输出的一个tensor  
dim是max函数索引的维度0/1，0是每列的最大值，1是每行的最大值  
函数会返回两个tensor，第一个tensor是每行的最大值；第二个tensor是每行最大值的索引。  

