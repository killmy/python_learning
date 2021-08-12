Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：

由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
进程之间可以并行不干扰

情况一：在主进程的任务与子进程的任务彼此独立的情况下，主进程的任务先执行完毕后，主进程还需要等待子进程执行完毕，然后统一回收资源。

情况二：如果主进程的任务在执行到某一个阶段时，需要等待子进程执行完毕后才能继续执行，就需要有一种机制能够让主进程检测子进程是否运行完毕，在子进程执行完毕后才继续执行，否则一直在原地阻塞，这就是join方法的作用

join()是卡着主进程而不是卡着子进程\

```python
from multiprocessing import Process
import os
import time
# 子进程要执行的代码
def run_proc1(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
def run_proc2(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    time.sleep(5)
    print('p2 结束')
if __name__ =="__main__":
    print('Parent process %s.' % os.getpid())
    p1 = Process(target=run_proc1,args=('run1',))
    p2 = Process(target=run_proc2,args=('run2',))

    print("start process")
    p1.start()
    p2.start()

    # 卡着主进程必须等p1，p2进程运行完毕
    time.sleep(1)
    p1.join()
    print('p1 运行完毕')
    p2.join()
    print('p2 运行完毕')

    print('运行完毕')
```
```
输出
Parent process 26562.
start process
Run child process run1 (26581)...
Run child process run2 (26582)...
p1 运行完毕
p2 结束
p2 运行完毕
运行完毕
```
可以看到子进程运行并行，而父进程被阻塞了
当注释掉join()函数后
```
Parent process 27329.
start process
Run child process run2 (27346)...
Run child process run1 (27345)...
p1 运行完毕
p2 运行完毕
运行完毕
p2 结束
```
父进程的运行没有受到影响，但是只有子进程完成运行，父进程才能继续执行

```python
# 进程池 pool
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
```
```
Parent process 27895.
Waiting for all subprocesses done...
Run task 0 (27912)...
Run task 1 (27914)...
Run task 2 (27913)...
Run task 3 (27915)...
Task 2 runs 1.35 seconds.
Run task 4 (27913)...
Task 0 runs 2.12 seconds.
Task 1 runs 2.44 seconds.
Task 3 runs 2.81 seconds.
Task 4 runs 2.61 seconds.
All subprocesses done.
```

Pool(num)决定进程的数量，当进程已满的时候，只有等其他进程执行完毕才能继续向进程内添加进程

Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。

我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
https://gitee.com/gfh123/sizhoutuxiangchuli/blob/%E6%AF%94%E8%B5%9B%E4%B8%93%E7%94%A8/g%E7%9A%84%E6%BA%90%E7%A0%81/main.py
参考我以前写的代码

```python
# 进程之间的通讯
from multiprocessing import Process,Queue
import multiprocessing as MP
import time


def send_image(name,information):
    'args输入数据的格式:[send_data],send_flag,stop_flag'
    while True:
        get_information = information.get()
        if get_information[1]==1:
            print('发送的数据为:',get_information[0])
        if get_information[2]==1:
            print('结束子进程')
            break

# 交换信息的载体
m = MP.Manager()
information = m.Queue() 
p1 = Process(target=send_image,args=('p1',information))
if __name__ == "__main__":
    p1.start()
    for i in range(5):
        information.put([i,1,0],False)
        time.sleep(1)
    information.put([0,0,1],False)
# 利用put 方法发送一次接收一次
```

```
输出
发送的数据为: 0
发送的数据为: 1
发送的数据为: 2
发送的数据为: 3
发送的数据为: 4
结束子进程
```

