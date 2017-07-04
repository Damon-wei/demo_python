#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 协程 coroutine

# 生产者-消费者模型

# 注意 变成generator的函数，在首次调用的时候执行，
# 遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def consumer():
    r = ''
    # 只有第一次会执行(启动生成器), 之后再调用生成器就会从yield处执行
    while True:
        n = yield r # 再次执行时从这里的yield继续执行, 将把produce传入的参数 n 赋给局部变量 n . 下轮循环再次遇到yield就会就将 r 返回给produce函数
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK' # 因为yield r 所以这个r会在下一次循环被返回给produce函数

def produce(c):
    c.send(None) # 启动生成器
    n = 0
    while n < 5:
         n = n + 1
         print('[PRODUCE] Producing %s...' % n)
         r = c.send(n) # 获取生成器consumer中由yield语句返回的下一个值
         print('[PRODUCER] Cousumer return: %s' % r)
    c.close()
c = consumer()
produce(c)

def f():
    print('start')
    a = yield 1
    print(a)
    print('middle...')
    b = yield 2
    print(b)
    print('next')
    c = yield 3
    print(c)

a = f()
a.send(None)
a.send(None)
a.send('msg')

# 深入理解 yield
# http://blog.csdn.net/haskei/article/details/54908853