from sqlalchemy import create_engine,Column,Integer,String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# (host='localhost', port=3306, user='root', password='guozhijia123', db='test_db')
Base = declarative_base()
class BaseTable(Base):
    # 创建的类内必须有一个或多个Column创建表内属性
    __tablename__ = "bookorm"   # 代表的是要创建的表名bookorm
    book_id = Column(Integer(), primary_key=True)
    # 创建的表字段，以及字段的属性（创建的字段内必须有一个是主键）
    book_name = Column(String(50), index=True)

class AuthorTable(Base):
    __tablename__ = "authororm"
    user_id = Column(Integer(), primary_key=True)
    user_name = Column(String(50), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

db_url = "mysql+pymysql://root:guozhijia123@localhost:3306/test_db?charset=utf8mb4"
engine = create_engine(db_url, echo=True, encoding="utf-8")
Base.metadata.create_all(engine)
