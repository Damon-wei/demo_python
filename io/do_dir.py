# 操作文件和目录
import os

print(os.name)
print(os.environ)
print(os.environ.get('classpath'))
# 查看当前目录的绝对路径
print(os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('D:\python\workspace\demo\io','testdir'))

# 然后创建一个目录:
os.mkdir('D:\python\workspace\demo\io\\testdir')

# 删掉一个目录:
os.rmdir('D:\python\workspace\demo\io\\testdir')

# 拆分路径时要通过 os.ptah.split() 函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.split('D:\python\workspace\demo\io\do_dir.py'))

# os.path.splitext()可以直接让你得到文件扩展名
print(os.path.splitext('D:\python\workspace\demo\io\do_dir.py'))

# 对文件重命名:
#os.rename('test.py','test.txt')

# 删掉文件:
#os.remove('test.txt')

# 列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])

# 列出当前目录下的所有.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
print()

# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
def search(dir=os.curdir, text="do"):
    for x in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, x)):
            if text in os.path.splitext(x)[0]:
                print('%s, %s' % (dir,x))
        if os.path.isdir(os.path.join(dir, x)):
            search(os.path.join(dir,x),text)

search('D:\python\workspace\demo','do')