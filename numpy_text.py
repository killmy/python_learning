'''
coding:utf-8
name:gfh
using:learn knowledge of numpy
'''
import typing
import numpy as np
from numpy import random
#创建一维数组
print(np.array([1,2,3]))

#创建二维数组
print(np.array([[1,2,3],
[4,5,6]]))

#创建多维数组
print(np.ones([2,3])) #2行3列
print(np.zeros([2,3]))#全1数组
print(np.empty([2,3]))#随机初始化

class Creat_numpy:
    def __init__(self) -> None:
        pass
    def creat_ones(self,row,col)->typing.Any:
        return np.ones([row,col])
numpy_test = Creat_numpy()
print(numpy_test.creat_ones(2,3))

#属性值
#维度数，2维，3维，4维等
a = np.ones([3,4])
print(a.ndim)
#行和列
print(a.shape)
#元素数 a.shape[0]xa.shape[1]
print(a.size)
#元素数据类型
print(a.dtype)
#创建具有特定类型的矩阵
b = np.zeros([2,3],dtype=np.int32)
print(b.dtype)
#返回每个元素的字节大小
print(a.itemsize)
print(b.itemsize)

#数组运算
class Array_Operation:
    def __init__(self) -> None:
        pass
    def Add(self,maxtri_1,maxtri_2) ->np.ndarray:
        'Add(self,maxtri_1,maxtri_2) ->np.ndarray\n  input two maxtir\n output the result of adding maxtri\n  对应元素相加'
        return maxtri_1+maxtri_2
    def Subtract(self,maxtri_1,maxtri_2) ->np.ndarray:
        'Add(self,maxtri_1,maxtri_2) ->np.ndarray\n  input two maxtir \n output the result of Subtracting maxtri\n  对应元素相减'
        return maxtri_1-maxtri_2
    def Devide(self,maxtri_1,maxtri_2)->np.ndarray:
        ' Devide(self,maxtri_1,maxtri_2)->np.ndarray\n  input two maxtri\n output the result of devide\n  对应元素相除'
        return maxtri_1/maxtri_2
    def Multiply(self,maxtri_1,maxtri_2)->np.ndarray:
        ' Multiply(self,maxtri_1,maxtri_2)->np.ndarray\n  input two maxtri\n output the result of multiply\n  对应元素相乘'
        return maxtri_1*maxtri_2
    def Maxtri_Multiply(self,maxtri_1,maxtri_2)->np.ndarray:
        ' Maxtri_Multiply(self,maxtri_1,maxtri_2)->np.ndarray\n  input two maxtri\n output the result of multiply\n  数组的矩阵乘法'
        #return maxtri_1.dot(maxtri_2)
        if maxtri_1.shape[1] == maxtri_2.shape[0]:
            return np.dot(maxtri_1,maxtri_2)
        else:
            print("请注意矩阵相乘原则")
a = np.array([[1,2,3],[4,5,6]]) #2x3
b = np.array([[4,5,6],[1,2,3]])#2x3
c = np.array([[1,2,3],[1,2,3],[1,2,3]])
array_op = Array_Operation()
print(array_op.Add(a,b))
print(array_op.Subtract(a,b))
print(array_op.Devide(a,b))
print(array_op.Multiply(a,b))
#数组运算和矩阵运算不同，数组运算有四则运算，对应元素进行运算
print(array_op.Maxtri_Multiply(a,c))

#数组自身的运算
#axis = 0是每一列，axis=1是每一行
a=np.array([[1,2,3],[4,5,6]])
print("输出最小值",a.min())
print(a.min(axis=0))
print(a.min(axis=1))
print("输出最大值",a.max())
print("输出最大值",a.max(axis=0))
print("输出最大值",a.max(axis=1))
print("输出所有元素之和",a.sum())
print("输出所有元素之和",a.sum(axis=0))
print("输出所有元素之和",a.sum(axis=1))

#对每个元素
#index_exp
#sqrt开根运算
#sqare平方运算
print("指数运算",np.exp(a))
print("开方运算",np.sqrt(a))
print("平方运算",np.square(a))

#随机数组
#生成伪随机数 seed()只要参数相同，生成的随机数就相同
num = 0
while(num<10):
    random.seed(6) #设置生成的随机数
    print(np.random.random())
    num+=1
#rand:生成样本在[0,1)之间，满足均匀分布,每个点生成的概率相同
print(np.random.rand(2,3))#2x3
#randn:平均值为0，方差为1的正太分布随机数
print(np.random.randn(2,3))
#randint:范围内的整数随机样本
print(np.random.randint(2,10,[2,3]))
#binomial 二项分布
print(np.random.binomial(6,0,[2,3]))
#beta；beta分布
print(np.random.beta(2,3))
#normal:高斯正太分布
print(np.random.normal(2,3))
for i in a.flat:
    print(i)