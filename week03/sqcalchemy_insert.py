from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, create_engine, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(50), index=True)

    # def __init__(self):
    #     print(f"Book_table(book_id='{self.book_id}', book_name={self.book_name}))")

    def __repr__(self):
        return f"Book_table(book_id='{self.book_id}', " \
               f"book_name='{self.book_name}'))"


class Author_table(Base):
    __tablename__ = "authororm"
    # primary_key  是否为主键
    # nullable   是否可以为空
    # autoincrement   是否自动增长
    # unique   是否唯一
    # default   默认值
    # Float    浮点数
    # Decimal   定点数
    # Boolean    bool值
    # Text
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


if __name__ == "__main__":
    # 创建表的引用对象
    book_table = Book_table()

    # 创建一个引擎
    db_url = "mysql+pymysql://root:guozhijia123@localhost:3306/test_db?charset=utf8mb4"
    engine = create_engine(db_url, echo=True, encoding="utf-8")

    # # 创建表（如果表已经存在，可以不执行改行，进行表的创建）
    # Base.metadata.create_all(engine)

    # 创建session
    SessionClass = sessionmaker(bind=engine)
    session = SessionClass()

    '''
    # # 对表数据进行插入操作，需要使用add函数
    # book_demo = Book_table(book_name='萧克的救赎', book_id=10000)
    # book_demo_01 = Book_table(book_name='萧克的救赎01')
    # book_demo_02 = Book_table(book_name='萧克的救赎02')
    # book_demo_03 = Book_table(book_name='萧克的救赎03')
    # book_demo_04 = Book_table(book_name='萧克的救赎04')
    # book_demo_05 = Book_table(book_name='萧克的救赎05')

    # session.add(book_demo)
    # session.add(book_demo_01)# add()函数是对表数据的insert操作
    # session.add(book_demo_02)
    # session.add(book_demo_03)
    # session.add(book_demo_04)
    # session.add(book_demo_05)
    # session.flush()
    # session.commit()
    '''

    '''
    # # 基本查询
    # # 查询一个表的所有数据
    # result = session.query(Book_table).all()
    # for result in session.query(Book_table):
    #     print(f"获取的结果：{result}")

    # # 查询一个表的数据，如果查询到一条或者多条数据的时候，返回第一条数据
    # result = session.query(Book_table).first()
    # print(f"获取的结果：{result}")

    # # one()、scalar()两个方法获取数据的时候，需要保证获取的数据是只有一条的，如果获取的数据多余一条，就会抛出异常
    # result = session.query(Book_table).one()
    # result = session.query(Book_table).scalar()
    # print(f"获取的结果：{result}")

    # # 获取指定字段列的数据
    # result = session.query(Book_table.book_name).first()
    # print(result)

    # # 对获取的数据进行排序
    # # 倒序
    # # for result in session.query(Book_table.book_name, Book_table.book_id).order_by(Book_table.book_id.desc()):
    # for result in session.query(Book_table.book_name, Book_table.book_id).order_by(desc(Book_table.book_id)):
    #     print(f"倒序result：{result}")
    # # 正序
    # for result in session.query(Book_table.book_name, Book_table.book_id).order_by(Book_table.book_id):
    #     print(f"正序result：{result}")

    # # 控制返回数据的条数
    # result = session.query(Book_table).order_by(Book_table.book_id.desc()).limit(3)
    # print([i.book_name for i in result])
    # for i in session.query(Book_table.book_name).order_by(Book_table.book_id.desc()).limit(3):
    #     print(i)
    #
    # session.commit()
    
        # # result = session.query(Book_table).filter(Book_table.book_id == 10000).first()
    # result = session.query(Book_table).filter(Book_table.book_id > 10000, Book_table.book_name == '萧克的救赎01').first()
    # print(result)
    # session.commit()

    # 使用sql内的and，or，not等连接词的操作
    from sqlalchemy import and_, or_, not_
    result = session.query(Book_table.book_name).filter(Book_table.book_id > 10000,
                                                        or_(
                                                            Book_table.book_name == '萧克的救赎02',
                                                            Book_table.book_name == '萧克的救赎04',
                                                            Book_table.book_name == '萧克的救赎05'
                                                        ),
                                                        Book_table.book_id < 11013,
                                                        and_(
                                                            Book_table.book_name == '萧克的救赎04'
                                                        ),
                                                        # not_(
                                                        #     Book_table.book_name != '萧克的救赎04'
                                                        # )
                                                        ).order_by(Book_table.book_id).limit(2)
    print([i for i in result])
    session.commit()
    '''

    # # 聚合函数的使用
    from sqlalchemy import func
    print(session.query(func.count(Book_table.book_name)).first())
    print(session.query(func.sum(Book_table.book_id)).first())
    print(session.query(func.max(Book_table.book_id)).first())
    print(session.query(func.min(Book_table.book_id)).first())
    print(session.query(func.avg(Book_table.book_id)).first())

