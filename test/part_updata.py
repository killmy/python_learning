# test *args 和**kwargs
# url:https://blog.csdn.net/weixin_37720172/article/details/78255177


def function(*args):
    print(args)
    print(args[0])
function(1,2)
function([1,2,3],4)
def function1(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
def function2(**kwargs):
    function1(**kwargs)
function2(a = 1,b =2)