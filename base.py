'''
coding:utf-8
name:gfh
using: python basic knowledge
'''
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