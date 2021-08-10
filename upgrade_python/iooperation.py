""" 
coding:utf-8
name:gfh
time:2021.08.01,afternoon
Summary:IO operation.
Reference link:https://www.liaoxuefeng.com/wiki/1016959663602400/1017604210683936
"""
#***read utf-8 files***#
# use open() os
# Raise 是用来抛出异常的
# import os
# path = './upgrade_python/unittest.py'
# if os.path.exists(path):
#     print("路径存在")
#     with open(path,'r') as f:
#         print(f.read())
# else:
#     print("检查路径")

# ***IO read and wright***#
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')
print(f.getvalue())
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
from io import BytesIO
f = BytesIO()
f.write('中文版'.encode('utf-8'))
print(f.getvalue())
f1 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f1.read())

# 序列化
# JSON
import json
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))
# load 针对文件 loads 针对内存

# json序列化
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    # 要返回字典才能序列化
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
# 这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：
s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))
# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
print(json.dumps(s,default=lambda obj:obj.__dict__))
