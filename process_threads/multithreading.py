# import time 
# #  线程函数库
# import threading

# # 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)

# if __name__ == "__main__":
#     print('thread %s is running...' % threading.current_thread().name)
#     t1 = threading.Thread(target=loop,name='LoopThread')
#     t2 = threading.Thread(target=loop,name='Loop2')
#     t1.start()
#     t2.start()
#     # 阻塞
#     t1.join()
#     t2.join()
#     print('thread %s ended.' % threading.current_thread().name)

# lock 避免数据错乱
# 先获取锁，然后修改数据，再释放锁，应该是执行玩那一块代码才能继续执行其他线程
# import time, threading

# # 假定这是你的银行存款:
# balance = 0
# lock = threading.Lock()

# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n

# def run_thread(n):
#     for i in range(100000):
#         # 先要获取锁:
#         lock.acquire()
#         try:
#             # 放心地改吧:
#             change_it(n)
#         finally:
#             # 改完了一定要释放锁:
#             lock.release()
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# ThreadLocal
import threading
# 创建全局Threadlocal对象
local_school = threading.local()

def process_student():
    std = local_school.student #局部变量student，应该随便取名
    print("{}/{}".format(std,threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

def process_student1():
    std = local_school.gfh #局部变量student，应该随便取名
    print("{}/{}".format(std,threading.current_thread().name))

def process_thread1(name):
    local_school.gfh = name
    process_student1()

t1 = threading.Thread(target=process_thread,args=('BOB',),name="T1")
t2 = threading.Thread(target=process_thread,args=('ABS',),name='T2')
t3 = threading.Thread(target=process_thread1,args=('gfh_thread',),name="T3")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
