'''
url:https://www.liaoxuefeng.com/wiki/1016959663602400/1017501655757856

'''
'''
正常情况下，当我们定义了一个class，
创建了一个class的实例后，
我们可以给该实例绑定任何属性和方法，
这就是动态语言的灵活性。先定义class：
'''
class Student(object):
    def __init__(self) -> None:
        super().__init__()

#给实例绑定属性
s = Student()
s.name = "Michel"
print(s.name)
#给实例绑定方法
def set_age(self,age):
    self.age = age
from types import MethodType
s.set_age=MethodType(set_age,s)#给实例绑定方法
s.set_age(25)
print(s.age)
#为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self,score):
    self.score = score
Student.set_score = set_score
s.set_score(100)
print(s.score)
#使用__slots__
'''
但是，如果我们想要限制实例的属性怎么办？
比如，只允许对Student实例添加name和age属性。
为了达到限制的目的，Python允许在定义class的时候，
定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
'''
'''
由于'score'没有被放到__slots__中，
所以不能绑定score属性，
试图绑定score将得到AttributeError的错误。

使用__slots__要注意，
__slots__定义的属性仅对当前类实例起作用，
对继承的子类是不起作用的：
'''
class Test(object):
    #限制了所有属性，只能具有定义的属性
    __slots__=('name','age','score')
    def __init__(self,score) -> None:
        self.score = score
t = Test(100)
print(t.score)
t.name = "std"
t.age=22
print(t.name)
print(t.age)

#使用@property
#在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
#这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：

class Student(object):
    def get_score(self):
        return self._score #有一个问题，未初始化不能直接使用，要在设置输入以后才能使用
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integar!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s = Student()
#未进行初始化的数值必须先进行初始化
s.set_score(10)
print(s.get_score())
#s.set_score(1000)

#Python内置的@property装饰器就是负责把一个方法变成属性调用的：
class Student1(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
#@property的实现比较复杂，我们先考察如何使用。
# 把一个getter方法变成属性，只需要加上@property就可以了，
# 此时，@property本身又创建了另一个装饰器@score.setter，
# 负责把一个setter方法变成属性赋值，于是，
# 我们就拥有一个可控的属性操作：
s = Student1()
s.score = 60
print(s.score)

#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

#多重继承
class Animal(object):
    def __init__(self) -> None:
        super().__init__()

#big class
class Mammal(Animal):
    def __init__(self) -> None:
        super().__init__()

class Bird(Animal):
    def __init__(self) -> None:
        super().__init__()

# kinds of animal
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

# Multiple inheritance
class Dog(Mammal,Runnable):
    pass

class Bat(Mammal, Flyable):
    pass
#通过多重继承，一个子类就可以同时获得多个父类的所有功能。

#MixIn
# 让Ostrich除了继承自Bird外，再同时继承Runnable。
# 这种设计通常称之为MixIn
import socketserver
#多进程TCP服务器
class MyTCPServer(socketserver.TCPServer, socketserver.ForkingMixIn):
    pass
#UDP 多线程
class MyUDPserver(socketserver.UDPServer,socketserver.ThreadingMixIn):
    pass

