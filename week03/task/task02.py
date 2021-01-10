from sqlalchemy import create_engine,Column,Integer,String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import pymysql
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class MemberTable(Base):
    __tablename__ = "member_info"
    member_id = Column(Integer(), primary_key=True, autoincrement=True, unique=True, comment='用户id')
    username = Column(String(50), nullable=False, comment='用户姓名')
    age = Column(Integer(), nullable=False, comment='年龄')
    birthday = Column(Integer(), nullable=False, comment='生日')
    gender = Column(String(50), nullable=False, comment='性别')
    education = Column(String(100), comment='学历')
    created_on = Column(DateTime(), default=datetime.now, comment='字段创新时间')
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now, comment='字段更新时间')

db_url = "mysql+pymysql://root:guozhijia123@localhost:3306/test_db?charset=utf8mb4"
engine = create_engine(db_url, echo=False, encoding="utf-8")# 创建连接mysql的引擎
Base.metadata.create_all(engine)# 使用sqlalchemy创建表

SessionClass = sessionmaker(bind=engine)
session = SessionClass()

def delete_member_info():
    # 清除表内所有的数据
    session.query(MemberTable).delete()
    session.commit()

# 使用sqlalchemy 插入数据
member_info = MemberTable()
memberInfo = MemberTable(member_id=1, username='guozhijia', age=18, birthday=19920304, gender="男", education="本科", created_on="2021-01-10 18:10:39", updated_on="2021-01-10 18:10:39")
session.add(memberInfo)
session.commit()

results = [i for i in session.query(MemberTable.username,MemberTable.member_id)]
print(results)

# 使用pymysql批量插入三条数据
def insertmany_func():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='guozhijia123', db='test_db')
    try:
        with db.cursor() as cursor:
            mysql = "insert into member_info (`member_id`, `username`, `age`, `birthday`, `gender`, `education`, `created_on`, `updated_on`) value (%s, %s, %s, %s, %s, %s, %s, %s)"
            datas = ((2, 'guodada', 11, 19901014, '男', '本科', '2021-01-10 18:10:39', '2021-01-10 18:10:42'),
                     (3, 'guodada', 11, 19901014, '男', '本科', '2021-01-10 18:10:39', '2021-01-10 18:10:42'),
                     (4, 'guodada', 11, 19901014, '男', '本科', '2021-01-10 18:10:39', '2021-01-10 18:10:42'))
            cursor.executemany(mysql, datas)
        db.commit()
    except Exception as e:
        print(f"insert error:{e}")
    finally:
        db.close()

# 使用pymysql查询数据
def fetchall_func():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='guozhijia123', db='test_db')
    try:
        with db.cursor() as cursor:
            sql = "select * from member_info"
            cursor.execute(sql)
            print(f"当前sql获取出来的数据行数：{cursor.rowcount}")
            results = cursor.fetchall()
            for i in results:
                print(i)
        db.commit()
    except Exception as err:
        print(f"fetchall error : {err}")
    finally:
        db.close()


if __name__ == "__main__":
    delete_member_info()
    insertmany_func()
    fetchall_func()

