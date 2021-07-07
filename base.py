'''
coding:utf-8
name:gfh
using: python basic knowledge
'''
import typing
import cv2

#类
class Student:
    student_Count = 0
    def __init__(self,name,age) -> None: #描述函数返回的类型
        '初始化参数'
        self.name = name
        self.age = age
        self.student_Count +=1
        pass
    def dist_student(self)->None:
        print("student name:",self.name,"student age:",self.age)
        pass
    def student_back(self,value)->typing.Any:
        
        if value==0:
            return self.name 
        elif value == 1:
            return self.age
        else:
            return self.student_Count
#继承
class New_student(Student):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        super().__init__(name, age)
    def dist_student(self)->None:
        '重写'
        print("student name is:",self.name,"student age is:",self.age)
        pass 
    def age_back(self)->typing.Any:
        return self.age
def test_explain(file,value)->int:
    'test_explain(file,value)->int \n (int)file:test data one  \n (int)value: test data two'
    if file>0 and value>0:
        return 1
    else:
        return 0

test_one = test_explain(1,1)
print("test_one: ",test_one)
# 任意整数
a = 0x55 #16
b = 10_000_000 #很大的数可以分开写
c = 0xff_123
Print_out = "a is:"+str(a)+" b is:"+str(b)
print(Print_out)

# 浮点数
a = 1.23e9 #科学计数法 1.23x10^9
b = 1.23e-9 #1.23x10^-9
c = 12/5 #精确计算
d = 12/5.1
e = 12//5#整除
Print_out = str(a)+" "+str(b)+" "+str(c)+" "+str(d)+" "+str(e)
print(Print_out)

#字符串
a = 'abc'
b = 'a\"tt\"' #\ 转义字符
c = r'a"b"' #默认不转义
d = r'a\"b"'
e = '\\\t\\\n\\\t\\'#\\-->\ \n换行
f = '''line1
... line2
... line3
'''
print(a+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+f+"\n")

