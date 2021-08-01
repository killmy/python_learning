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
