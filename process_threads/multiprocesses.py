# # os使用fork调用进程
# import os
# # Only works on Unix/Linux/Mac:
# # os.getpid
# print("父进程ID:",os.getpid())
# # 创建一个子进程
# pid = os.fork()
# print('当前进程 ID =',os.getpid()," pid=",pid)
# #根据 pid 值，分别为子进程和父进程布置任务
# if pid == 0:
#     print('子进程, ID=',os.getpid()," 父进程 ID=",os.getppid())
# else:
#     print('父进程, ID=',os.getpid()," pid=",pid)

# multiprocessing

# from multiprocessing import Process
# import os
# import time
# # 子进程要执行的代码
# def run_proc1(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
# def run_proc2(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#     time.sleep(5)
#     print('p2 结束')
# if __name__ =="__main__":
#     print('Parent process %s.' % os.getpid())
#     p1 = Process(target=run_proc1,args=('run1',))
#     p2 = Process(target=run_proc2,args=('run2',))

#     print("start process")
#     p1.start()
#     p2.start()

#     # 卡着主进程必须等p1，p2进程运行完毕
#     time.sleep(1)
#     # p1.join()
#     print('p1 运行完毕')
#     # p2.join()
#     print('p2 运行完毕')

#     print('运行完毕')

# # 进程池 pool
# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

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