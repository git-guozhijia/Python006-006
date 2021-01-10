from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, create_engine, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(50), index=True)


if __name__ == "__main__":
    book_table = Book_table()

    db_url = "mysql+pymysql://root:guozhijia123@localhost:3306/test_db?charset=utf8mb4"
    engine = create_engine(db_url, echo=False, encoding="utf-8")

    SessionClass = sessionmaker(bind=engine)
    session = SessionClass()

    # # 更新操作
    # # query = session.query(Book_table).filter(Book_table.book_id == 10000).update({Book_table.book_name : f"sdasdadasda"})
    # query = session.query(Book_table.book_name)
    # query = query.filter(Book_table.book_id > 10000)
    # query.update({Book_table.book_name : f"new_book"})
    # print([i for i in query.all()])
    # session.commit()

    # delete()函数删除数据的操作
    query = session.query(Book_table)
    query = query.filter(Book_table.book_id == 11001)
    # query.delete()
    session.delete(query.one())
    session.commit()


