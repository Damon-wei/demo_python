#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from io import StringIO
# StringIO顾名思义就是在内存中读写str。
# write to StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())
# getvalue()方法用于获得写入后的str。

# read from StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
