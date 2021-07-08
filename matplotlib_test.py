from re import X
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.defchararray import title
#直接显示Matplotlib绘制的图，使用jupyter notebook 或者 jupyter qtconsole的时候
#%matplotlib inline 
np.random.seed(42) #保证可重复性
x= np.random.randn(30)#生成正太分布，一维30个
y = np.random.rand(30)
z = np.random.rand(30)
w = np.random.rand(30)
o = 2*x + 0.5
print(x)
#标题
plt.title("titleB")
#坐标轴
plt.xlabel("X")
plt.ylabel("Y")
#画图
plt.plot(x,'r--o',linewidth = 1.5,label='o')#红色，虚线，点表示
plt.plot(y,'b--x',linewidth=1.0,label='b')
#图例
plt.legend()
#matlab通过切换窗口设置窗口信息所以不用变量的函数,此函数库变量无用
fig = plt.figure("titleA")
ax1 = fig.add_subplot(221,title="A")
plt.xlabel("x")
plt.ylabel('y')
plt.plot(x,'r--o')
ax2 = fig.add_subplot(222,title="B")
plt.xlabel("x")
plt.ylabel('y')
labels = [ 'Dos ','Cats ','Birds ' ] 
sizes = [15 , 50 , 35]
plt.pie(sizes ,explode=(0, 0, 0.1) , labels=labels, autopct ='%1.1f%%',
startangle=90 ) 
plt.axis('equal')
ax3 = fig.add_subplot(223,title="C")
#直方图
a = np.random.randn(1000)
plt.xlabel("x")
plt.ylabel('y')
plt . hist(a , bins=20 , color='g') 
ax4 = fig.add_subplot(224,title="D")#落在区间内的个数
plt.xlabel("x")
plt.ylabel('y')
plt.scatter(x,w,c='g',marker='o')
plt.tight_layout()
plt.savefig("1.png")
plt.show() #永远不会关闭，除非q
#plt.draw()#可关闭
# plt.pause(1)
# plt.close()
