'''
url: https://www.liaoxuefeng.com/wiki/1016959663602400/1017598873256736
name:gfh
time:2021.7.24
'''
# try: except: finally
try:
    print('try...')
    r = 10/0
    print('result:',r)
except ZeroDivisionError as e:
    print('expect',e)
finally:
    print('finally...')
print('END')

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

'''
Python的错误其实也是class，
所有的错误类型都继承自BaseException，
所以在使用except时需要注意的是，
它不但捕获该类型的错误，还把其子类也“一网打尽”。
比如：
'''
