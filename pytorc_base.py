'''
date:
name:gh
using:learn pytorch_base
'''
import torch
import numpy as np
import matplotlib
from torch import tensor
from torch.functional import Tensor

#torch.tensor()只能·产生固定元素的tensor
a = torch.tensor([2,3],dtype=torch.float32)
print(a)
#创建特定类型的tensor第二种方法
b = torch.FloatTensor(2,3)
c = torch.FloatTensor([1,2,3,4])
print(b)
print(c)
d = torch.IntTensor(2,3)
f = torch.IntTensor([1,2,3,4])
print(d)
print(f)
#生成0~1之间的浮点数
e = torch.rand(2,3)
h = np.random.rand(2,3)
print(e)
print(h)
i = torch.tensor(h)
print(i)
#平均值0，方差1的正态分布随机数
a = torch.randn(2,3)
b = np.random.randn(2,3)
print(a)
print(b)
print(torch.tensor(b))

#生成自定义起始和步长，生成浮点数,这个函数限制变成了torch.arrage()
a = torch.arange(1,10,0.5)
print(a)

#生成全0矩阵
a = torch.zeros(2,3)#只能生成浮点型
b = np.zeros([2,3],dtype=np.int)#生成任意类型
c = np.zeros([2,3],dtype=np.float)
print(a)
print(torch.tensor(b))
print(torch.tensor(c))

#生成全1矩阵
d = torch.ones(2,3,4)
e = np.ones([2,3,4],dtype=np.float)
print(d)
print(torch.tensor(e))

#对tensor内的矩阵做绝对运算
a = torch.arange(-1,1,0.5)
print(a)
print(torch.abs(a))

#tensor加法,对应元素相加
a = torch.randn(2,3)
b = torch.randn(2,3)
c = 10
print(a)
print(b)
print(torch.add(a,b))
print(a.add(b))
print(a.add(c))

#限定输入输出边界,超过边界的值将被限定为边界值
a = torch.randn(2,3)
print(a)
print(torch.clamp(a,-0.1,0.1))

#对应元素相除,div_()时in-place操作，值会被存入a中
a = torch.randn(2,3)
b = torch.randn(2,3)
c = 10
print(a)
print(b)
print(torch.div(a,b))
print(a.div_(b))
print(a.div_(c))

#对应元素相乘
a = torch.randn(2,3)
b = torch.randn(2,3)
print(a)
print(a.mul_(b))
print(a.mul_(10))#上步骤的结果存入了a
print(torch.mul(a,10))
print(torch.mul(a,10))#只有in-place操作才会把结果存入a中

#元素求幂
a = torch.randn(2,3)
print(a)
print(a.pow_(2))

#矩阵乘法
a = torch.randn(2,3)
b = torch.randn(3,2)
print(a)
print(b)
print(a.mm(b))

#矩阵与向量的乘法1,矩阵，2，向量
a = torch.randn(2,3)
b = torch.randn(3)
print(a)
print(b)
print(a.mv(b))
# print(a.mm(b)) a.mm()不能矩阵乘向量


