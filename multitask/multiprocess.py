from multiprocessing import Pool
import os, time ,random

print('Process (%s) Strat...'% os.getpid())
# Only works on UNix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s'% (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s)' %(os.getpid(), pid))

print('\n')
# multiprocessing模块
from multiprocessing import Process

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' %(name, os.getpid()))

# if __name__ == '__main__':
#     print('Parent process %s '% os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     p.start()
#     p.join()
#     print('Child process end.')

# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

# Pool
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程


def long_time_task(name):
    print('Run task %s (%s)'%(name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(8)
    for i in range(9):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。