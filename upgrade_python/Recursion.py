'''
url:https://www.liaoxuefeng.com/wiki/1016959663602400/1017268131039072
递归
'''
#n!递归
#不断调用同一个函数，但是有表达式eg.n*fact，参数改变，直到达到条件
def fact(n):
    if n==1:
        return 1 #结束递归
    return n*fact(n-1)
print(fact(5))
#optimization
#尾调用,返回只调用自身，并没有包含表达式
def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num-1,num*product) 
def fact(n):
    return fact_iter(n,1)
print(fact(5))
#尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
