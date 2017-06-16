# datetime
# datetime是Python处理日期和时间的标准库。
from datetime import datetime

# 获取当前日期和时间
now = datetime.now()
print(now)
print(type(now))


# 获取指定日期和时间
dt = datetime(2017,6,15,16,47,56)
print(dt)


# datetime转换为timestamp(时间戳)
# 你可以认为：
# timestamp = 0 1970-1-1 00:00:00 UTC+0:00
# 对应的北京时间是：
# timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00

timestamp = dt.timestamp() # 把datetime转换为timestamp
print(timestamp)

# 注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
# 某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，
# 这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。


# timestamp转换为datetime
# 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：
print(datetime.fromtimestamp(timestamp))

# 注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。
# 本地时间是指当前操作系统设定的时区。例如北京时区是东8区，则本地时间：
# 2015-04-19 12:20:00
# 实际上就是UTC+8:00时区的时间：
# 2015-04-19 12:20:00 UTC+8:00
# 而此刻的格林威治标准时间与北京时间差了8小时，也就是UTC+0:00时区的时间应该是：
# 2015-04-19 04:20:00 UTC+0:00
# timestamp也可以直接被转换到UTC标准时区的时间：

print(datetime.fromtimestamp(timestamp)) # 本地时间
print(datetime.utcfromtimestamp(timestamp)) # UTC时间


# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(type(cday),':',cday)

# datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
print()

# datetime加减
#
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。
# 加减可以直接用+和-运算符，不过需要导入timedelta这个类：
from datetime import datetime, timedelta
now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now + timedelta(days=1))
print(now + timedelta(days=2,hours=12))


# 本地时间转换为UTC时间
#
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：

from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
print(now)
datetime.datetime(2015, 5, 18, 17, 2, 10, 871012)
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dt)
datetime.datetime(2015, 5, 18, 17, 2, 10, 871012, tzinfo=datetime.timezone(datetime.timedelta(0, 28800)))
# 如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。


# 时区转换
#
# 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# 2015-05-18 09:05:12.377316+00:00

# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# 2015-05-18 17:05:12.377316+08:00

# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# 2015-05-18 18:05:12.377316+09:00

# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)
# 2015-05-18 18:05:12.377316+09:00

# 时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
# 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
# 注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。


# 小结
#
# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
#
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。