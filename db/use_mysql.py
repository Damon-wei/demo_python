# 导入 mysql 驱动
import pymysql
# 创建连接
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='360360', db='test', charset='utf8')
cursor = conn.cursor()
# 创建 user 表
cursor.execute('create table user (id varchar(20) primary key, name varchar (20))')
# 插入一行记录
cursor.execute('insert into user(id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount
# 提交事务
conn.commit()
cursor.close()
# 查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()