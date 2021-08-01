import logging
import os
import yaml
from logging import config
def use_yaml_config(default_path='./upgrade_python/logging.yaml', default_level=logging.INFO):
    path = default_path
    if os.path.exists(path):
        print('in')
        with open(path, 'r', encoding = 'utf-8') as f:
            config = yaml.load(stream=f, Loader=yaml.FullLoader)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
if '__main__' == __name__:
    use_yaml_config(default_path='./upgrade_python/logging.yaml')
    # root的logger
    root = logging.getLogger()
    # 子记录器的名字与配置文件中loggers字段内的保持一致
    # loggers:
    #   my_testyaml:
    #       level: DEBUG
    #       handlers: [console, info_file_handler,error_file_handler]
    my_testyaml = logging.getLogger("my_module")
    print("rootlogger:", root.handlers)
    print("selflogger", my_testyaml.handlers)
     # 判断子记录器与根记录器的handler是否相同
    print(root.handlers[0] == my_testyaml.handlers[0])
    my_testyaml.info("INFO")
    my_testyaml.error('ERROR')
    my_testyaml.debug("rootDEBUG")
    # 注意配置的级别，级别不够不会显示，根据级别可以筛选默认的级别
    # 可以为每一个文件配置一个log
    # root.info("INFO")
    # root.error('ERROR')
    # root.debug("rootDEBUG")   
    # my_testyaml.info("INFO")