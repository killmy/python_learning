'''
url:https://www.liaoxuefeng.com/wiki/1016959663602400/1017328655674400
高阶函数
'''

def fab(n):
    if n==1:
        return 1
    return n*fab(n-1)
print(fab(3))
#递归范围函数本身而不是函数计算式则可以避免堆栈的问题
def fab_optimization(n,output=1):
    if n == 1:
        return output*1
    return fab_optimization(n-1,n*output)
print(fab_optimization(3))

#high order function-->input parameters have function
f = abs #将变量f定义为abs函数
print(f(-10))
#define high order function
def high(x,y,f):
    return f(x)+f(y)
print(high(-1,1,f))

'''
map()函数接收两个参数，一个是函数，一个是Iterable(只要是可迭代的即可)，
map将传入的函数依次作用到序列的每个元素，
并把结果作为新的Iterator返回。
'''
origin = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#use [for]
print([pow(x,2) for x in origin])
g1 = (pow(x,2) for x in origin)
print(g1)
# print(next(g1))
# for s in range(2):
#     for i in g1:
#         print(i)
#     print("21")
#python iteration 是单项的，只能使用一次
#enumerate 只是增加索引
#需要返回迭代器
#正确的循环迭代器
for s in range(2):
    for i,k in enumerate(g1):
        print(i,k)
def pow2(x):
    return pow(x,2)
g2 = map(pow2,origin)
print(g2)
for i in range(2):
    for k in map(pow2,origin):
        print(k)
#迭代器是一次性的，只能不断的去返回迭代器才能循环，用到返回函数
'''
看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
'''
from functools import reduce
import functools
def add(x,y):
    return x+y
print(reduce(add,[1,3,5,7,9]))
#sum求和
print(sum([1,2,3,4]))
def fn(x,y):
    return x*10+y
print(reduce(fn,[1,2,3,4,5]))
#str turn into int

def charnum(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
#reduce 和 map后面跟的都是可迭代的
print(reduce(fn,map(charnum,'1234')))

#Python内建的filter()函数用于过滤序列。
'''
和map()类似，filter()也接收一个函数和一个序列。
和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。
'''
#删偶留奇
def is_odd(n):
    return n%2==1#返回True or Flase
print(list(filter(is_odd,[1,2,3,4,5,6])))
from collections.abc import Iterable
print(isinstance(filter(is_odd,[1,2,3,4,5,6]),Iterable))
'''
可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
注意到filter()函数返回的是一个Iterator，
也就是一个惰性序列，所以要强迫filter()完成计算结果，
需要用list()函数获得所有结果并返回list。
'''

#Python内置的sorted()函数就可以对list进行排序：
print(sorted([36, 5, -12, 9, -21]))
#此外，sorted()函数也是一个高阶函数，
# 它还可以接收一个key函数来实现自定义的排序，
# 例如按绝对值大小排序：
print(sorted([36, 5, -12, 9, -21], key=abs))
#这样，我们给sorted传入key函数，即可实现忽略大小写的排序：
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax+n
        return ax
    return sum
f = lazy_sum(1,3,5,7,9)
print(f)
print(f())
'''
在这个例子中，我们在函数lazy_sum中又定义了函数sum，
并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时
，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
'''
#不能将返回函数用在循环中，循环结束后再执行返回函数
#匿名函数
f = lambda x:pow(x,2)
print(f)
print(f(5))

#装饰器,就是定义一个返回函数的函数，中间加上一些东西，保留原函数的功能
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log 
def now():
    print('2015')
# now = log(now)
now()

#偏函数用于固定参数
int2 = functools.partial(int,base=2)

