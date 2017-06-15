import time, threading

# 由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，
# Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：

# 新线程执行的方法
def loop():
    print('thread %s is running... '% threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s is ended.'% threading.current_thread().name)

print('thread %s is running... '% threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s is ended.'% threading.current_thread().name)

# 每个进程默认都会启动一个线程，即为主线程MainThread
