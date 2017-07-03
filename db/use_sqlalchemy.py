from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义user对象
class User(Base):
    # 表名:
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多
    books = relationship()

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))


# 初始化数据库连接
db_config = {
    'user':'root',
    'passwd':'360360',
    'host':'127.0.0.1:3306',
    'db':'test',
    'charset':'utf8'
}
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+pymysql://%s:%s@%s/%s?charset=%s' % (db_config['user'],
                                                           db_config['passwd'],
                                                           db_config['host'],
                                                           db_config['db'],
                                                           db_config['charset']))
# 创建 DBSession 类型
DBSession = sessionmaker(bind=engine)

# 创建 Session 对象
session = DBSession()
# 创建新 User 对象
new_user = User(id='5', name='Bob')
# 添加到 session
session.add(new_user)
# 提交即保存到数据库
session.commit()
session.close()

# 有了ORM，查询出来的可以不再是tuple，而是User对象
session = DBSession()
user = session.query(User).filter(User.id == '5').one()
print('type:', type(user))
print('name:', user.name)
session.close()