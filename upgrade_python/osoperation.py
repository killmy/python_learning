""" 
coding:utf-8
name:gfh
time:2021.08.01,afternoon
Summary:OS operation.
Reference link:https://www.liaoxuefeng.com/wiki/1016959663602400/1017604210683936
"""
# os 操作系统
# import os
# print(os.name)
# # 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# # 获取详细信息
# print(os.uname())

# # 环境变量
# # 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
# print(os.environ)
# # 要获取某个环境变量的值，可以调用os.environ.get('key')：
# print(os.environ.get("PATH"))

# # 操作文件和目录
# # 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
# a = os.path.abspath('.')
# print(a)
# c = os.path.join(a,'Processes_Threads')
# print(c)
# if os.path.exists(c):
#     pass
# else:
#     os.mkdir(c)
# if os.path.exists(c):
#     os.rmdir(c)
# else:
#     pass
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
""" 
os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')
 """
#  os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
""" 
os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')
 """
#  这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
# 文件操作使用下面的函数。假定当前目录下有一个test.txt文件：
# mkdir 只能创建文件夹
# d = 'multiplythreads.txt'
# e = os.path.join(c,d)
# print(e)
# if os.path.exists(e):
#     pass
# else:
#     os.mkdir(e)
# f = 'multiplythreads.py'
# h = os.path.join(c,f)
# if os.path.exists(h):
#     pass
# else:
#     os.rename(e,h)

# 序列化
# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# Python提供了pickle模块来实现序列化。
# 首先，我们尝试把一个对象序列化并写入文件：
import os
import pickle
path = './upgrade_python/test.txt'
d = dict(name='Bob', age=20, score=88)
data_bytes = pickle.dumps(d)
print(data_bytes)
if os.path.exists(path):
    with open(path,'wb') as f:
        pickle.dump(d,f)
    f.close()
else:
    pass
if os.path.exists(path):
    with open(path,'rb') as f:
        d = pickle.load(f)
        print(d)
    f.close
else:
    pass


