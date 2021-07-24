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
