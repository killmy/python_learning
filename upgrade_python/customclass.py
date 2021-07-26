'''
转载url:https://www.liaoxuefeng.com/wiki/1016959663602400/1017590712115904
my name:gfh
'''
'''
看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
__slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。
除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。
'''

# __str__
class Student(object):
    def __init__(self,name) -> None:
        super().__init__()
        self.name = name

print(Student('g'))
# <__main__.Student object at 0x7f72c85d2dc0>

class Student(object):
    def __init__(self,name) -> None:
        super().__init__()
        self.name = name
    def __str__(self) -> str:
        return  'Student object (name: %s)' % self.name
    # __repr__=__str__

print(Student('g'))
# Student object (name: g)

'''
直接显示变量调用的不是__str__()，而是__repr__()，
两者的区别是__str__()返回用户看到的字符串，
而__repr__()返回程序开发者看到的字符串，
也就是说，__repr__()是为调试服务的。
解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的
'''

# __iter__
'''
如果一个类想被用于for ... in循环，类似list或tuple那样，
就必须实现一个__iter__()方法，该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法
拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
'''
class Fib(object):
    def __init__(self) -> None:
        super().__init__()
        self.a = 0
        self.b = 1
    def __iter__(self):
        '实例本身就是迭代对象，故返回自己'
        return self
    def __next__(self):
        self.a ,self.b = self.b,self.a+self.b
        if self.a>20:
            raise StopIteration()
        return self.a
a = Fib()
for n in a:
    print(n)

# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
    def __init__(self) -> None:
        super().__init__()
    def __getitem__(self,n):
        a,b=1,1
        for x in range(n):
            a,b = b,a+b
        return a
f = Fib()
print(f[0])
# __getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

'''
也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。

'''

# __getattr__  动态链接
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：
# 调用不存在的属性时，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。

class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99

# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值：
s = Student()
print(s.name)
print(s.score)

# 返回函数也是完全可以的：
class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
# f = lambda x:x+1 x输入，x+1输出

# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。

'''
此外，注意到任意调用如s.abc都会返回None，
这是因为我们定义的__getattr__默认返回就是None。
要让class只响应特定的几个属性，我们就要按照约定，
抛出AttributeError的错误
'''
class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

'''
这实际上可以把一个类的所有属性和方法调用全部动态化处理了，
不需要任何特殊手段。
'''
'''
果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
利用完全动态的__getattr__，我们可以写出一个链式调用：
'''
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__
print(Chain().status.user.timeline.list)

#__call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
 
s = Student('g')
s()
# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
print(callable(Student))
print(callable([1, 2, 3]))

#============================================== #
#                                                 enum class                                           #
#============================================== #
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

#print the value of Month.Jan
print(Month['Jan'].value) 
print(Month.Jan.value)

# print all of the value
for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)
# value属性则是自动赋给成员的int常量，默认从1开始计数。
# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
print(Weekday.Tue.value)
for name, member in Weekday.__members__.items():
    print(name,'==>',member)

#============================================== #
#                                                 metaclass                                          
#============================================== #
# class is dynamicly created  by type function
def fn(self,name='world'):
    print("Hello,%s" %name)
Hello = type('Hello',(object,),dict(hello=fn))
h = Hello()
h.hello()