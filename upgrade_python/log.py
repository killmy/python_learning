# coding:utf-8
#using for log
#url:https://blog.csdn.net/pansaky/article/details/90710751
#https://www.jb51.net/article/88449.htm
# import logging

#                                          Info Grade
# INFO
'''logging.basicConfig(level=logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail")
logger.info("finish")
'''
#DEBUG
'''
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger = logging.getLogger(__name__)
logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail")
logger.info("finish")
'''
# debug、info、warning、error以及critical。


#                                   write log in document and terminal

# logger = logging.getLogger(__name__)
# # set grade
# logger.setLevel(level=logging.INFO)
# # save path
# handler = logging.FileHandler("./upgrade_python/log.txt")
# handler.setLevel(logging.INFO)
# #set formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
# # logger中添加StreamHandler，可以将日志输出到屏幕上，
# console = logging.StreamHandler()
# console.setFormatter(formatter)
# console.setLevel(logging.INFO)
# logger.addHandler(console)

# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")

# log rotating
# 按文件大小划分
# from logging.handlers import RotatingFileHandler
# logger = logging.getLogger('log test')
# logger.setLevel(level = logging.INFO)
# #定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
# rHandler = RotatingFileHandler("./upgrade_python/log_contian.txt",maxBytes = 1*1024,backupCount = 3)
# rHandler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# rHandler.setFormatter(formatter)
 
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# console.setFormatter(formatter)
 
# logger.addHandler(rHandler)
# logger.addHandler(console)
 
# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")

# 按时间划分
# import time
# import logging
# import logging.handlers

# #初始化工作
# logging.basicConfig()
# #myapp
# logger = logging.getLogger('mylog')
# logger.setLevel(logging.INFO)

# # 3 files  1s a file 
# thandler = logging.handlers.TimedRotatingFileHandler('./upgrade_python/logtime.txt',when='S',interval=1,backupCount=3)
# thandler.suffix = "%Y-%m-%d_%H-%M-%S.log"
# thandler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# thandler.setFormatter(formatter)
# # terminal
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# console.setFormatter(formatter)

# # add handler
# logger.addHandler(thandler)
# logger.addHandler(console)
# i = 0
# logger.info("file 1")
# time.sleep(1)
# logger.info('file 2')
# time.sleep(2)
# logger.info('file 3')
# time.sleep(1)
# logger.info('file 4')
# time.sleep(1)
# logger.info('file 5')
# # all 4 files

# import logging
# logging.basicConfig()
# logger = logging.getLogger('test log')

# # settle handle
# handler = logging.FileHandler("log.txt")
# handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
 
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
 
# logger.addHandler(handler)
# logger.addHandler(console)
 
# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")

# try:
#     open("sklearn.txt","rb")
# except (SystemExit,KeyboardInterrupt):
#     raise
# except Exception:
#     logger.error("Faild to open sklearn.txt from logger.error",exc_info = True)
#     logger.exception("Failed to open sklearn.txt from logger.exception")
# logger.info("Finish")

# 多模块使用log
# 每个模块都可以单独使用logging.getLogger()
# import logsub
# logger = logging.getLogger("mainModule")
# logger.setLevel(level = logging.INFO)
# handler = logging.FileHandler("log.txt")
# handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
 
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# console.setFormatter(formatter)
 
# logger.addHandler(handler)
# logger.addHandler(console)
 
 
# logger.info("creating an instance of subModule.subModuleClass")
# a =logsub.SubModuleClass()
# logger.info("calling subModule.subModuleClass.doSomething")
# a.doSomething()
# logger.info("done with  subModule.subModuleClass.doSomething")
# logger.info("calling subModule.some_function")
# logsub.som_function()
# logger.info("done with subModule.some_function")

# use json
# import json
# import logging.config
# import os

# def setup_logging(default_path = "./upgrade_python/logging.json",default_level = logging.INFO,env_key = "LOG_CFG"):
#     path = default_path
#     value = os.getenv(env_key,None)
#     if value:
#         path = value
#     if os.path.exists(path):
#         with open(path,"r") as f:
#             config = json.load(f)
#             print(config)
#             logging.config.dictConfig(config)
#     else:
#         logging.basicConfig(level = default_level)
 
# def func():
#     logging.info("start func")
 
#     logging.info("exec func")
 
#     logging.info("end func")
 
# if __name__ == "__main__":
#     setup_logging(default_path = "./upgrade_python/logging.json")
#     func()
#     try:
#         open("sklearn.txt","rb")
#     except (SystemExit,KeyboardInterrupt):
#         raise
#     except Exception:
#         logging.error("Faild to open sklearn.txt from logging.error",exc_info = True)
# 文件配置或者代码有一些问题