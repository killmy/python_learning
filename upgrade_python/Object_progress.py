import typing
from numpy import core
from numpy.lib.function_base import delete


class Student():
    def __init__(self) -> None:
        pass
bart = Student()
print(bart)
print(Student)
bart.name = "abc"
print(bart.name)

#class
class Student1():
    def __init__(self,name,core) -> None:
        'name:姓名,core:得分'
        self.name = name
        self.core = core
    def print_data(self)->None:
        'print_data(self)->None 打印输出'
        print("%s:%s" %(self.name,self.core))
        print("{}:{}".format(self.name,self.core))
    def get_grade(self):
        if self.core>90:
            print("A")
        elif self.core>80:
            print('B')
        elif self.core >70:
            print('C')
        else:
            print('D')
#实例
bart1 = Student1('g',99)
print(bart1.name,bart1.core)
bart1.print_data()

'''
在Class内部，可以有属性和方法，
而外部代码可以通过直接调用实例变量的方法来操作数据，
这样，就隐藏了内部的复杂逻辑。
但是，从前面Student类的定义来看，
外部代码还是可以自由地修改一个实例的name、score属性：
'''
'''
果要让内部属性不被外部访问，
可以把属性的名称前加上两个下划线__，
在Python中，实例的变量名如果以__开头，
就变成了一个私有变量（private），只有内部可以访问
，外部不能访问，所以，我们把Student类改一改：
'''
class Student3():
    def __init__(self,name,score) -> None:
        self.__name = name 
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    def get_name(self)->typing.Any:
        return self.__name
    def get_score(self)->typing.Any:
        return self.__score
    def set_score(self,score):
        self.__score = score

'''
需要注意的是，在Python中，变量名类似__xxx__的，
也就是以双下划线开头，并且以双下划线结尾的，
是特殊变量，特殊变量是可以直接访问的，
不是private变量，所以，不能用__name__、
__score__这样的变量名。
有些时候，你会看到以一个下划线开头的实例变量名，
比如_name，这样的实例变量外部是可以访问的，
但是，按照约定俗成的规定，当你看到这样的变量时，
意思就是，“虽然我可以被访问，但是，
请把我视为私有变量，不要随意访问”。

双下划线开头的实例变量是不是一定不能从外部访问呢？
其实也不是。不能直接访问__name是因为
Python解释器对外把__name变量改成了
_Student__name，所以，
仍然可以通过_Student__name来访问__name变量：
好像不太行
但是强烈建议你不要这么干，
因为不同版本的Python解释器可能会把__name改成不同的变量名。
'''
bart = Student3('g',90)


class Origin_G():
    def __init__(self,score,grade) -> None:
        self.__name = 'g'
        self.score = score
        self.__grade = grade
        self.test = 't'
    def back_name(self):
        return self.__name
    def change_name(self,name):
        self.__name = name
class G1(Origin_G):
    def __init__(self, score, grade) -> None:
        super().__init__(score, grade)
        self.score = score
        self.__grade = grade
    def change_grade(self,grade):
        self.__grade = grade
    def back_grade(self):
        return self.__grade
class G2(Origin_G):
    def __init__(self, score, grade) -> None:
        super(G2,self).__init__(score, grade)
        #self.__name = 
    # def back_name(self):
    #     str = 'name is :'+ self.__grade
    #     return str
g1 = G1(90,'A')
print(g1.score)
print(g1.back_name())

#内部不能直接调用，但是外部可以调用,如果要调用就要进行重写,
# 但是不用强继承就可以调用非初始化里面的值
g2 = G2(90,'A')
print(g2.score)
print(g2.test)
print(g2.back_name())

'''
要理解什么是多态，我们首先要对数据类型再作一点说明。
当我们定义一个class的时候，我们实际上就定义了一种数据类型。
我们定义的数据类型和Python自带的数据类型，
比如str、list、dict没什么两样：
'''
print(isinstance(g2,G2))
print(isinstance(g2,Origin_G))
g0 = Origin_G(12,"F")
print(isinstance(g0,G2))
#子类的实例数据类型可以是子类也可以是父类，但是父类的实例数据类型一定只有父类
#子类获得父类所有功能

#多态的意思是子类继承父类所有的功能，不需要重新定义
'''
对于静态语言（例如Java）来说，如果需要传入Animal类型，
则传入的对象必须是Animal类型或者它的子类，
否则，将无法调用run()方法。

对于Python这样的动态语言来说，
则不一定需要传入Animal类型。
我们只需要保证传入的对象有一个run()方法就可以了：
'''
#使用type()函数判断数据类型,isinstance()函数用来判断继承很方便
#总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

#使用dir()
'''
如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
'''
print(dir(123))

'''
类似__xxx__的属性和方法在Python中都是有特殊用途的，
比如__len__方法返回长度。
在Python中，如果你调用len()函数试图获取一个对象的长度，
实际上，在len()函数内部，它自动去调用该对象的__len__()方法，
所以，下面的代码是等价的：
'''
print(len('ABC'))
print("ABC".__len__())

#len属性
class Origin_Test():
    def __init__(self) -> None:
        pass
    def __len__(self):
        return 100
A = Origin_Test()
print(len(A))

'''
仅仅把属性和方法列出来是不够的，
配合getattr()、setattr()以及hasattr()，
我们可以直接操作一个对象的状态：
hasattr(实例,'属性')是否具有某种属性
setattr(实例,'属性',value) 设置属性
getattr(实例，属性)得到某种属性的值
getattr(实例，属性,value)错误时返回某种固定的属性
'''
#但是，如果Student类本身需要绑定一个属性呢？
# 可以直接在class中定义属性，这种属性是类属性，
# 归Student类所有：

#实例属性可以自己添加，但是类属性无法更改。

class Test():
    name = "G"
s = Test()
print(s.name)
print(Test.name)
s.name = "T"
print(s.name)
print(Test.name)
del s.name
print(s.name)
#实例添加属性
s.name1 = 5
print(s.name1)
'''
从上面的例子可以看出，在编写程序的时候，
千万不要对实例属性和类属性使用相同的名字，
因为相同名称的实例属性将屏蔽掉类属性，
但是当你删除实例属性后，再使用相同的名称，
访问到的将是类属性。
'''
