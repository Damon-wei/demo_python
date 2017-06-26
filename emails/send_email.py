# SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。

from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
import smtplib


def _fromat_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = '1020430800@qq.com'
password = '***********'
to_addr = '18612124664@163.com'
smtp_server = 'smtp.qq.com'

# 发送纯文本或带HTML的邮件
def sendEmail():
    msg = MIMEText('hello,send by Python...', 'plain', 'utf-8')

    # 发送HTML邮件
    # 如果我们要发送HTML邮件,在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了
    # msg = MIMEText( '<html><body><h1>Hello</h1><p>send by <a href="http://www.python.org">Python</a> </p></body></html>','html', 'utf-8')

    # 注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，
    # 传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
    msg['From'] = _fromat_addr('Python爱好者 <%s>' % from_addr)
    msg['To'] = _fromat_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()

    server = smtplib.SMTP_SSL(smtp_server, 465)  # SMTP 的默认端口是 25/465
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

    # 我们编写了一个函数_format_addr()来格式化一个邮件地址。
    # 注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码。
    # msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。

    # 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
    # SMTP协议就是简单的文本命令和响应。
    # login()方法用来登录SMTP服务器，
    # sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，
    # 邮件正文是一个str，as_string()把MIMEText对象变成str。


# 发送带附件/图片的邮件
def sendEmail_file():
    # 带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，
    # 所以，可以构造一个MIMEMultipart对象代表邮件本身，
    # 然后往里面加上一个MIMEText作为邮件正文，
    # 再继续往里面加上表示附件的MIMEBase对象即可
    msg = MIMEMultipart()
    msg['From'] = _fromat_addr('Python爱好者 <%s> '% from_addr)
    msg['To'] = _fromat_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候......', 'utf-8').encode()

    # 邮件正文是MIMEText
    msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

    # 添加附加就是加上一个MIMEBase，从本地读取
    with open(r'D:\python\workspace\demo\test.jpg', 'rb') as f:
        # 设置附件的MIME和文件名，这里是jpg类型
        mime = MIMEBase('image', 'jpg', filename='test.jpg')
        # 加上必要的头信息
        mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来
        mime.set_payload(f.read())
        # 用Base64编码
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart
        msg.attach(mime)

    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    # 发送图片
    # 如果要把一个图片嵌入到邮件正文中怎么做？直接在HTML邮件中链接图片地址行不行？答案是，大部分邮件服务商都会自动屏蔽带有外链的图片，因为不知道这些链接是否指向恶意网站。
    # 要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，然后，在HTML中通过引用src = "cid:0"
    # 就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid: x即可。
    # 把上面代码加入MIMEMultipart的MIMEText从plain改为html，然后在适当的位置引用图片：
    # msg.attach(MIMEText('<html><body><h1>Hello</h1><p><img src="cid:0"></p></body></html>', 'html', 'utf-8'))


# 发送同时支持HTML和Plain格式的邮件
def sendEmail_HTML_Plain():
    # 利用MIMEMultipart就可以组合一个HTML和Plain，
    # 要注意指定subtype是alternative
    msg = MIMEMultipart('alternative')

    msg.attach(MIMEText('hello', 'plain', 'utf-8'))
    msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))

    msg['From'] = _fromat_addr('Python爱好者 <%s>' % from_addr)
    msg['To'] = _fromat_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()

    server = smtplib.SMTP_SSL(smtp_server, 465)  # SMTP 的默认端口是 25/465
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


# 发送加密SMTP的邮件
def sendEmail_SSL():
    # 加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。
    # Gmail的SMTP端口是587

    msg = MIMEText('hello', 'plain', 'utf-8')

    msg['From'] = _fromat_addr('Python爱好者 <%s>' % from_addr)
    msg['To'] = _fromat_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()

    server = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail的SMTP端口是587
    server.starttls()
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

if __name__ == '__main__':
    sendEmail_SSL()

# 小结
# 使用Python的smtplib发送邮件十分简单，只要掌握了各种邮件类型的构造方法，正确设置好邮件头，就可以顺利发出。
# 构造一个邮件对象就是一个Messag对象，如果构造一个MIMEText对象，就表示一个文本邮件对象，
# 如果构造一个MIMEImage对象，就表示一个作为附件的图片，
# 要把多个对象组合起来，就用MIMEMultipart对象，
# 而MIMEBase可以表示任何对象。它们的继承关系如下：
# Message
# +- MIMEBase
#    +- MIMEMultipart
#    +- MIMENonMultipart
#       +- MIMEMessage
#       +- MIMEText
#       +- MIMEImage
# 这种嵌套关系就可以构造出任意复杂的邮件。你可以通过email.mime文档查看它们所在的包以及详细的用法。