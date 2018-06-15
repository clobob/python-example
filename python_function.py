#coding:utf-8
"""
def say_hello(name):
    print('hello I am ' +name)
say_hello('while')
say_hello('for')

"""
#使用位置参数举例


def say_hello(name,age):
    print('hello %s is %d years old '%(name,age))

say_hello('while',18,)

#参数个数错误
try:
    say_hello('while')
except (TypeError),x:
    print x


#默认值参数用法举例

def default_value(name='default'):
    print('这是一个默认值函数，name= %s'%(name))

default_value()
print '给定参数后，不再使用默认值参数'
default_value('自定义值')


#参数组： 1. 元组参数组;--*  2. 字典参数组 -- **
def multiple_params(*names):
    print(names)

print '随意个数参数传入函数看如何处理'
multiple_params('while','for','mk','rm')
multiple_params(*range(10))
multiple_params()

#字典参数组举例

def dict_params(**kw):
    print(kw)
print '字典参数组，传递参数后，函数获取到的参数样例'
dict_params()
dict_params(name='while')
dict_params(**{'age':18})


#python 函数划分

a = lambda x,y:x+y

print 'lambda函数举例, python2 不可以使用print方法， python3可以使用print 方法'
print(a(1,2))

print(a(22,101))

# 返回型函数->有返回值; 计算型函数->没有返回值

def num():
    print 'this is num'
    print(1)

def num_v1():
    print 'this is num1'
    return 1

num()
print num_v1()+3


