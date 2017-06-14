import time, threading

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
