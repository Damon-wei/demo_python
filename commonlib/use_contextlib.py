# contextlib

# 在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们。
# 正确关闭文件资源的一个方法是使用try...finally：
try:
    f = open('D:/python/workspace/demo/commonlib/use_contextlib.py', 'r', encoding='utf-8')
    f.read()
finally:
    if f:
        f.close()

# 因为写 try...finally 非常繁琐，我们可以使用 with 语句允许我们非常方便的使用资源：
with open('D:/python/workspace/demo/commonlib/use_contextlib.py', 'r', encoding='utf-8') as f:
    f.read()


# 并不是只有open()函数返回的fp对象才能使用with语句。
# 实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的。
class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('error')
        else:
            print('end')

    def query(self):
        print('Query info about %s' % self.name)


with Query('Bob') as q:
    q.query()

# 但是编写__enter__和__exit__仍然很繁琐，
# 因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：
from contextlib import contextmanager


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s' % self.name)

@contextmanager
def create_query(name):
    print('begin')
    q = Query(name)
    yield q
    print('end')
# @contextmanager这个decorator接受一个generator，用yield语句
# 把with ... as var把变量输出出去，然后，with语句就可以正常地工作了：
with create_query('Bob') as q:
    q.query()

# 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。例如：
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)

with tag('h1'):
    print('hello')
    print('world')

# 代码的执行顺序是：
# 1.with语句首先执行yield之前的语句，因此打印出<h1>；
# 2.yield调用会执行with语句内部的所有语句，因此打印出hello和world；
# 3.最后执行yield之后的语句，打印出</h1>。
# 因此，@contextmanager让我们通过编写generator来简化上下文管理。


# @closing
# 如果一个对象没有实现上下文，我们就不能把它用于with语句。
# 这个时候，可以用closing()来把该对象变为上下文对象。
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://www.baidu.com')) as page:
    for l in page:
        print(l)