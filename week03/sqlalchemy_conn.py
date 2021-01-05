from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,ForeignKey

# (host='localhost', port=3306, user='root', password='guozhijia123', db='test_db')
# echo=True 代表打开调试模式
# mysql 代表链接的数据库类型
# pymysql  代表链接mysql使用的api方式
engine = create_engine("mysql+pymysql://root:guozhijia123@localhost:3306/test_db", echo=True)

# 创建元数据，元数据初始化，直接链接数据库
metadata = MetaData(engine)

book_table = Table("book", metadata,
                   Column("id", Integer, primary_key=True),
                   Column("name", String(20)),
                   )

author_table = Table("author", metadata,
                   Column("id", Integer, primary_key=True),
                   Column("book_id", None, ForeignKey("book.id")),
                   Column("author_name", String(120), nullable=False),
                   )

try:
    metadata.create_all()
except Exception as err:
    print(f"create table err:{err}")

