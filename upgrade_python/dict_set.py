''''
coding:utf-8
url:https://www.liaoxuefeng.com/wiki/1016959663602400/1017104324028448
'''

#dict
d = {'a':68,'c':69}
print(d)
d['d'] = 60
print(d)
print('b' in d)
print(d.get('b'),d.get('b',-1))
d.pop('d')
print(d)

#set
s = set([1,2,3])
s1 = set([2,3,4])
s2 = set(['a','b','c'])
print(s,s1,s2)
print(s&s1)
s.add('a')
print(s)
s.remove('a')
print(s)