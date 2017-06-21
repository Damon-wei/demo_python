# 正则表达式

# 直接给字符就是精确匹配
# \d 匹配一个数字
# \w 匹配一个字母或数字
# \s 匹配一个空格（也包括Tab等空白符）
# . 匹配任意字符
#
# * 表示任意个字符
# + 表示至少一个字符
# ? 表示0或1个字符
# {n} 表示n个字符
# {n,m} 表示n-m个字符
#
# 特殊字符需要加 \ 转义
# 如：\d{3}\-\d{3,8} 可以匹配'010-12345'这样的固话号码。

# [] 可以表示范围
# [0-9a-zA-Z\_] 可以匹配一个数字、字母或者下划线
# [0-9a-zA-Z\_]+ 可以匹配至少有一个数字、字母或者下划线组成的字符串
# [a-zA-Z\_][0-9a-zA-Z\_]* 可以匹配由字母或下划线开头，后接任意个由数字字母下划线组成的字符串，也就是Python合法的变量
# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）
# A|B 可以匹配A或B，所以(P|p)ython 可以匹配 Python 或 python
# ^ 表示行的开头，^\d 表示必须以数字开头
# $ 表示行的结束，\d$ 表示必须以数字结束


# re模块
#
# 由于python的字符串本身就是用 \ 转义，所以在匹配正则的时候直接用 r 前缀就不用考虑转义问题了。

import re

print(re.match(r'^\d{3}\-\d{3,8}$','010-123456'))
print(re.match(r'^\d{3}\-\d{3,8}$','010-123456').group(0))

# 切分字符串
print(re.split(r'\s+','a  b    c'))
print(re.split(r'[\s\,]+','a ,, b ,   c'))
print(re.split(r'[\s\,\;]+','a ,, b ;;,   c'))

# 分组
# 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）。
# ^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：
r = re.match(r'^(\d{3})-(\d{3,8})','010-123456')
print(r.group(0))
print(r.group(1))
print(r.group(2))
print(r.groups())

# 如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。
# 注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。
# groups()直接获取所有子串

# 提取时间
t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:'
             r'(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:'
             r'(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())


# 贪婪匹配
#
# 最后需要特别指出的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。举例如下，匹配出数字后面的0：

re.match(r'^(\d+)(0*)$', '102300').groups()
# >>> ('102300', '')
# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
re.match(r'^(\d+?)(0*)$', '102300').groups()
# >>> ('1023', '00')


# 编译
#
# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：
#
# 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
#
# 用编译后的正则表达式去匹配字符串。
#
# 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：

# 先编译:
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
re_telephone.match('010-12345').groups()
# >>> ('010', '12345')
re_telephone.match('010-8086').groups()
# >>> ('010', '8086')
# 编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。



# 练习
#
# 请尝试写一个验证Email地址的正则表达式。可以验证并提取出带名字的Email地址：
# someone@gmail.com
# bill.gates@microsoft.com

r = r'^([0-9a-zA-Z][\w\_\.-]+)\@\w+\.[a-z]*$'
m = re.match(r, 'bill.gates@microsoft.com')
if m:
    print('email:',m.group(0))
    print('username:',m.group(1))
else:
    print('flase')