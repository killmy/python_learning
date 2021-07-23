'''
coding:utf-8
url:https://www.liaoxuefeng.com/wiki/1016959663602400/1017269965565856
'''
#slice
#list
L=['a','b','c','d']
print(L[0:3])
print(L[1:3])
print(L[:3])
L = list(range(100))
print(L[:10])
print(L[-10:])
print(L[:10:2])

#tuple
L = (1,2,3,4)
print(L[:3])

#string
L = 'abcdefgijklmnopqrstuvwxy'
print(L[:10:2])

#前两个参数觉得范围，后一个参数决定步长

#iter
#dict 
d = {'a':1,'b':2,"c":3}
for key in d:
    print(key,d[key])

#list
d = [1,2,3,45,6]
for num in d:
    print(num)

#string 
d = 'abc'
for ch in d:
    print(ch)

#那么，如何判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断：
from collections.abc import Iterable
#isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
print(isinstance('abc',Iterable))
print(isinstance(123,Iterable))

#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i,value in enumerate(['a','b','c']):
    print(i,value)


#list generate
print(list(range(1,11)))
print([x*x for x in range(1,11)])
print([pow(x,2) for x in range(1,11) if x%2==0])
#还可以使用两层循环，可以生成全排列：
print([m+n for m in "AB" for n in "XYZ"])
#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k,'=',v)
print([(k,v) for k,v in d.items()])
d = [(1,2),(3,4),(5,6)]
for k,v in d:
    print(k,v)

#for 循环本身就是一种迭代
#迭代器
g = (pow(x,2) for x in range(1,11) )
print(next(g))
print("已经迭代了一次")
for n in g:
    print(n)

#比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
#1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#yield 把函数变成生成器
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n+=1
    return 'done'
o = fib(6)
print(o)
for data in o:
    print(data)
#iter()把可数据变成迭代生成的 ,变成迭代器只能生成但个数据
d = {'s':1,'s1':2}
for s,v in d.items():
    print(s,v)
d = iter(d.items())
for s in d:
    print(s)