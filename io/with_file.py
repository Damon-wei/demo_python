#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件读写
# try:
#     f = open('D:\python\workspace\demo\\fact.py', "r")
#     print(f.read())
# finally:
#     f.close()

# with open('D:\python\workspace\demo\\fact.py', "r") as f:
#     print(f.read())

# with open(r'D:\python\workspace\demo\\fact.py') as f:
#     print(f.read())

# 如果文件很小，read()一次性读取最方便；
# 如果不能确定文件大小，反复调用read(size)比较保险；
# 如果是配置文件，调用readlines()最方便；

# with open('D:\python\workspace\demo\\fact.py', "r") as f:
#     for line in f.readlines():
#         print(line.strip())  # 去掉末尾的'\n'

# file-like Object
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
# 除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。

# 二进制文件
# 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。
# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

# with open('D:\python\workspace\demo\\202169-106.jpg', "rb") as f:
#     print(f.read())

# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数.
with open('D:\python\workspace\demo\gbk.txt', "r", encoding='utf-8',errors='ingore') as f:
    print(f.read())

# 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
with open('D:\python\workspace\demo\\test.txt', "w", encoding='utf-8') as f:
    print(f.write('写文件'))


from datetime import datetime
with open('test.txt','w',encoding='utf-8') as f:
    f.write('今天是：')
    f.write(datetime.now().strftime("%Y-%m-%d"))

with open('test.txt','r',encoding='utf-8') as f:
    print('open for read...')
    print(f.read())