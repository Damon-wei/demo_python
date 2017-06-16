import base64

# Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，
# 好处是编码后的文本数据可以在邮件正文、网页等直接显示。
# 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？
# Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。

b = base64.b64encode(b'binary\x00string')
print(b)
print(base64.b64decode(b))
print()

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
a = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
b = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(a)
print(b)
print(base64.urlsafe_b64decode(b))
print()

# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
# 标准Base64:
# 'abcd' -> 'YWJjZA=='
# 自动去掉=:
# 'abcd' -> 'YWJjZA'

# 去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，
# 因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。

def safe_base64_decode(s):
    if not len(s) % 4 == 0:
        s = s + b'=' * (4 - len(s) % 4)
    return base64.b64decode(s)
print(safe_base64_decode(b'YWJjZA=='))
print(safe_base64_decode(b'YWJjZA'))

# 编码时是3个字节一组，所以字节缺失可能有一个或两个，也就是等号最多有一个或两个。
# 用字符串长度对4进行取余，如果余数为3，表示去掉了一个等号；余数为2，表示去掉了两个等号。
# 然后拼接上去掉的等号再进行解码就行了。