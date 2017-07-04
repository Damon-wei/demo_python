import asyncio
import threading

# asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，
# 然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。

def fun1():
    @asyncio.coroutine
    def hello():
        print('Hello world! (%s)' % threading.currentThread())
        # 异步调用asyncio.sleep(1):
        yield from asyncio.sleep(1)
        print('Hello again!(%s)' % threading.currentThread())

    # 获取EventLoop:
    loop = asyncio.get_event_loop()
    tasks = [hello(), hello()]
    # 执行coroutine
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


# 用asyncio的异步网络连接来获取sina、sohu和163的网站首页
def fun2():
    @asyncio.coroutine
    def wget(host):
        print('wget %s...' % host)
        connect = asyncio.open_connection(host, 80)
        reader, writer = yield from connect
        header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
        writer.write(header.encode('utf-8'))
        while True:
            line = yield from reader.readline()
            if line == b'\r\n':
                break
            print('%s header > %s ' % (host, line.decode('utf-8').rstrip()))
        writer.close()

    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

# fun1()
fun2()